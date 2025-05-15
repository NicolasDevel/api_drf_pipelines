from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer


# Create your views here.
@api_view(['GET'])
def list_products(request):
    ''' Listar productos '''
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data, status.HTTP_200_OK)

@api_view(['POST']) #Guardar
def store_product(request):
    ''' Crear un producto '''
    serializer = ProductSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
    else:
        return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)

@api_view(['GET', 'PUT', 'DELETE'])
def detail_product(request, product_id):
    ''' Obteener, actualizar o eliminar un producto especifico '''

    product = get_object_or_404(Product, id = product_id)

    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data, status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK )
        else:
            return Response(serializer.errors, status.HTTP_422_UNPROCESSABLE_ENTITY)
    
    if request.method == 'DELETE':
        product.delete()
        return Response( status = status.HTTP_204_NO_CONTENT)
