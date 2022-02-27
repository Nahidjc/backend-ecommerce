from django.urls import path
from base.views import order_views as views


urlpatterns = [
    path('add/', views.addOrderItems, name='add-order'),
    path('<str:pk>/', views.getOrderItems, name='users-order'),
]
