from django.urls import path
from base.views import product_views as views


urlpatterns = [

    path('', views.getProducts, name='products'),
    path('<str:pk>', views.getProduct, name='product'),
    path('<str:pk>/review/', views.createProductReview, name='product-reveiw'),
    path('delete/<str:pk>/', views.deleteProduct, name='delete-product'),
    path('create/', views.createProduct, name='create-product'),
    path('update/<str:pk>/', views.updateProduct, name='update-product'),
    path('upload/', views.uploadImage, name="image-upload"),
]
