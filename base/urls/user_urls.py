from django.urls import path
from base.views import user_views as views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,

)


urlpatterns = [
    path('login', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('register', views.registerUser,
         name='register'),
    path('profile/', views.getUserProfile, name='users-profile'),
    path('', views.getUsers, name='users'),

]
