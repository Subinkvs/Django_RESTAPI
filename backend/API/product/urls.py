from django.urls import path
from .views import  ProductDetailAPIView, ProductListAPIView
 
urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductListAPIView.as_view())
]