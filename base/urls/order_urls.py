from django.urls import path
from base.views import order_views as views


urlpatterns = [
    path('add/', views.addOrderItems, name='add-order'),
    path('<str:pk>/', views.getOrderItems, name='users-order'),
    path('my/orders/', views.MyOrderList, name='myorders'),
    path('total/orders/', views.TotalOrderList, name='totalorders'),
    path('<str:pk>/pay/', views.updateOrderToPaid, name='pay'),
]
