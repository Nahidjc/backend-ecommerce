from django.urls import path
from base import views
urlpatterns = [
    path('/routes', views.getRoutes, name='routes'),
    path('/products', views.getProducts, name='products')
]
