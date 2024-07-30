import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import  Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

# Create your views here.
@api_view(["POST"])
def api_call(request, *args, **kwargs):
    """
    DRF API VIEW
    """    
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        prod = serializer.save()
        print(prod)
        print(serializer.data)
        return Response(serializer.data, status=201)
    else:
        return Response(serializer.errors, status=400)
