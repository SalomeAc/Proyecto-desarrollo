from django.http import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ProductoSerializer, UserProductoSerializer
from .models import  Producto, ProductoUsuario
from rest_framework import status
import json
import logging




    
class ProductoView(viewsets.ModelViewSet):
    serializer_class=ProductoSerializer
    queryset=Producto.objects.all()
    
class ProductosUsuariosView(viewsets.ModelViewSet):
    serializer_class= UserProductoSerializer
    queryset = ProductoUsuario.objects.all()

@api_view(['GET'])
def search_products(request):
    
    criteria = request.GET.get('criteria')
    value = request.GET.get('value')
    
    print("criteria= ",criteria)
    print("value= ",value)
    
    if not criteria or not value:
        return Response({"error": "Missing criteria or value"}, status=400)

    # Mapea los criterios a los campos del modelo
  
    
    match criteria:
        case 'categoria_id':
            value=int(value)
        case 'cantidad_producto':
            value=int(value)
            
        case 'estado_producto':
            
            value = value.lower()=='activo'
            
            
        case 'precio':
            value=float(value)
            
        
        case _:
            value=value.lower()
    


    filter_args = {criteria: value}
    products = Producto.objects.filter(**filter_args)
    serializer = ProductoSerializer(instance=products, many=True)  
    for product in serializer.data:
        product['foto_producto'] = request.build_absolute_uri(product['foto_producto'])
    return Response({"products": serializer.data}, status=status.HTTP_200_OK)



@api_view(['GET'])
def search_users_products(request):
    
    criteria = request.GET.get('criteria')
    value = int(request.GET.get('value'))
    
    print("criteria= ",criteria)
    print("value= ",value)
    
    if not criteria or not value:
        return Response({"error": "Missing criteria or value"}, status=400)

    
    filter_args = {criteria: value}
    t_pu = ProductoUsuario.objects.filter(**filter_args)
    print ("t_PU", t_pu )

    return Response(find_user_product(t_pu), status=status.HTTP_200_OK)



def find_user_product(ids_products):
    
    productos = []
    
    for product in ids_products:
         print(product)
         id_product = product.id
         print(id_product)
         product_filter = Producto.objects.filter(id=id_product)
         serializer = ProductoSerializer(instance=product_filter, many=True)
         productos.append(serializer.data)
    return productos[0]
    


    