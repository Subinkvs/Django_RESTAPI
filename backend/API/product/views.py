from .serializer import  ProductSerializer
from app.models import Product
from rest_framework import generics
from rest_framework.response import Response

# Create your views here.
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# class ProductCreateAPIView(generics.CreateAPIView):
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
    
#     def perform_create(self, serializer):
#         print(serializer.validated_data)
#         title = serializer.validated_data.get('title')
#         content = serializer.validated_data.get('content')
#         content = title
#         serializer.save(content=content)
    
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer