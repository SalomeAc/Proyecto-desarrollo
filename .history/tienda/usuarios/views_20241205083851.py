from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

class UsuarioView(viewsets.ModelViewSet):
    serializer_class=UsuarioSerializer
    queryset=User.objects.all()
    
@api_view(['POST'])
def login(request):
    
    user=get_object_or_404(User,username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"error":"invalid password"},status=status.HTTP_400_BAD_REQUEST)
    
    token,created= Token.objects.get_or_create(user=user)
    serializer=UsuarioSerializer(instance=user)
    
    return Response({"token":token.key, "user":serializer.data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
        
    serializer=UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        
        user=User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        
        token=Token.objects.create(user=user)
        
        return Response({'token':token.key,'user':serializer.data},status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def updateUser(request):
    try:
         # Obtén al usuario autenticado (o añade lógica para especificar uno)
        data = request.data
        print(data['password'])
        user=get_object_or_404(User,id= data['id'])
        
        # Actualizar campos del usuario
        
        user.username = data['username']
        user.email = data['email']
        user.is_staff=data['is_staff']
        user.is_superuser=data['is_superuser']
        
       
        if 'password' in data and data['password']:
            user.set_password(data['password'])
        
        user.save()

        # Serializar los datos actualizados
        serializer = UsuarioSerializer(user)

        return Response({'message': 'Usuario actualizado correctamente', 'user': serializer.data}, status=status.HTTP_200_OK)
    
    except User.DoesNotExist:
        return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

    except Exception as e:
        return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    print(request.user.id)
    return Response("you are login with {}".format(request.user.username),status=status.HTTP_200_OK)


@api_view(['GET'])
def search_users(request):
    
    criteria = request.GET.get('criteria')
    value = request.GET.get('value')
    
    print("criteria= ",criteria)
    print("value= ",value)
    
    match criteria:
        case 'id':
            value=int(value)
        case 'is_staff':
            value=bool(value)
            
        case 'is_superuser':
            
            value = bool(value)
                
        case _:
            value=value
    
    if not criteria or not value:
        return Response({"error": "Missing criteria or value"}, status=400)

    filter_args = {criteria: value}
    users = User.objects.filter(**filter_args)
    serializer = UsuarioSerializer(instance=users, many=True)  
    return Response({"users": serializer.data}, status=status.HTTP_200_OK)
    

