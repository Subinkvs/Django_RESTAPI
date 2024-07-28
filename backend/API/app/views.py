import json

from django.shortcuts import render
from django.http import JsonResponse
from .models import  Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ProductSerializer

# Create your views here.
@api_view(["GET"])
def api_call(request, *args, **kwargs):
    """
    DRF API VIEW
    """    
    product = Product.objects.all().order_by("?").first()
    data = {}
    if product:
        data = ProductSerializer(product).data
    return Response(data)
