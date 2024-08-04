from django.urls import path
from .views import  ProductDetailAPIView, ProductListCreateAPIView, ProductUpdateAPIView, ProductDestroyAPIView, ProductMixinList
 
urlpatterns = [
     path('', ProductListCreateAPIView.as_view()),
     path('<int:pk>/',  ProductDetailAPIView.as_view()),
     path('<int:pk>/update/', ProductUpdateAPIView.as_view()),
     path('<int:pk>/delete/', ProductDestroyAPIView.as_view())
     ]