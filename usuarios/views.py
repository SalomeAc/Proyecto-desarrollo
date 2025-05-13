from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import UsuarioSerializer
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.decorators import authentication_classes, permission_classes,action
from rest_framework.permissions import IsAuthenticated,BasePermission,IsAdminUser
from rest_framework.authentication import TokenAuthentication
from django_recaptcha.fields import ReCaptchaField
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.mail import send_mail
import requests

class IsStaffAndCanOnlyReadOrCreate(BasePermission):
    """
    Permite que usuarios con is_staff=True solo puedan leer o crear.
    """
    def has_permission(self, request, view):
        user = request.user
        if user.is_staff and not user.is_superuser:
            return view.action in ['list', 'retrieve','search_users']
        if user.is_superuser:
            return  True
        return False
        

    

class UsuarioView(viewsets.ModelViewSet):
    serializer_class=UsuarioSerializer
    queryset=User.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated, IsStaffAndCanOnlyReadOrCreate]

    @action(detail=False, methods=['POST'])
    def register(self, request):
        serializer = UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            user = User.objects.get(username=serializer.data['username'])
            user.set_password(serializer.data['password'])
            user.save()

            token = Token.objects.create(user=user)
            return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['PUT'])
    def update_user(self, request):
        try:
         
            data = request.data
            print(data['password'])
            user=get_object_or_404(User,id= data['id'])
            
        
            
            user.username = data['username']
            user.email = data['email']
            user.is_staff=data['is_staff']
            user.is_superuser=data['is_superuser']
            
        
            if 'password' in data and data['password']:
                user.set_password(data['password'])
            
            user.save()

            
            serializer = UsuarioSerializer(user)

            return Response({'message': 'Usuario actualizado correctamente', 'user': serializer.data}, status=status.HTTP_200_OK)
    
        except User.DoesNotExist:
            return Response({'error': 'Usuario no encontrado'}, status=status.HTTP_404_NOT_FOUND)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
      
         

    @action(detail=False, methods=['GET'])
    def search_users(self, request):
        criteria = request.GET.get('criteria')
        value = request.GET.get('value')
    
        print("criteria= ",criteria)
        print("value= ",value)
        
        match criteria:
            case 'id':
                value=int(value)
            case 'is_staff':
                value = value=='true'
                
            case 'is_superuser':
                
                value = value=='true'
            case 'username':
                
                criteria = 'username__icontains'
                    
            

                
        
    

        filter_args = {criteria: value}
        users = User.objects.filter(**filter_args)
        serializer = UsuarioSerializer(instance=users, many=True)  
        return Response({"users": serializer.data}, status=status.HTTP_200_OK)
    
    
    
@api_view(['POST'])
def login(request):
    print(request.data)
    user=get_object_or_404(User,username=request.data['username'])
    
    if not user.check_password(request.data['password']):
        return Response({"error":"invalid password"},status=status.HTTP_400_BAD_REQUEST)
    
    token= Token.objects.get_or_create(user=user)
    serializer=UsuarioSerializer(instance=user)
    
    return Response({"token":token.key, "user":serializer.data}, status=status.HTTP_200_OK)

@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def verify_email(request):
    return Response({'message': 'Email verificado exitosamente'}, 
                    status=status.HTTP_200_OK)
    
        
   
        
def send_verification_email(user):
    token= Token.objects.get_or_create(user=user)
    verification_link = f"https://classsmart-mu.vercel.app/verify_Email/{token}"
    send_mail(
        'Verify your email',
        f'Click the link to verify: {verification_link}',
        'andresdavid.ortega@gmail.com',
        [user.email],
        fail_silently=False,
    )



@api_view(['POST'])
def register_user(request):
    data=request.data
    
    captcha=data['captcha']
    
    recaptcha_field=ReCaptchaField()
    
    try:
        recaptcha_field.validate(captcha)
        print('captchavalido')
    except ValidationError :
        return Response({'success':False,'error':'CAPTCHA invalido'},status=400)
    
    print(data['user'])
    usuario=data['user']
    usuario['is_staff']=False
    usuario['is_superuser']=False
    serializer = UsuarioSerializer(data=usuario)
    print(serializer.is_valid())
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=serializer.data['username'])
        user.set_password(serializer.data['password'])
        user.save()
        send_verification_email(user)

        token = Token.objects.get_or_create(user=user)
        return Response({'token': token.key, 'user': serializer.data}, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   

        
        
        
