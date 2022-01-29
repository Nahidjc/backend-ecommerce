from django.urls import path
from base import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)


urlpatterns = [
    path('users/login', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('routes', views.getRoutes, name='routes'),
    path('products', views.getProducts, name='products'),
    path('products/<str:pk>', views.getProduct, name='product')
]
