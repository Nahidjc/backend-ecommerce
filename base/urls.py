from django.urls import path
from base import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)


urlpatterns = [
    path('users/login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('users/register', views.registerUser,
        name='register'),
    path('routes', views.getRoutes, name='routes'),
    path('users/profile/', views.getUserProfile, name='users-profile'),
    path('users/', views.getUsers, name='users'),
    path('products', views.getProducts, name='products'),
    path('products/<str:pk>', views.getProduct, name='product')
]
