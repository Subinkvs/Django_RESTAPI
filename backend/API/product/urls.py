from django.urls import path
from .views import ProductCreateAPIView, ProductDetailAPIView
 
urlpatterns = [
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('', ProductCreateAPIView.as_view())
]