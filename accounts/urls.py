from django.urls import path
from . import views



urlpatterns = [
    path('addedjucation/',views.addedjucation,name='addedjucation'),
    path('addexperience/',views.addexperience,name='addexperience'),
    path('create/',views.create,name='create'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('login/',views.login_view,name='login'),
    path('profile/<int:pk>/',views.profile,name='profile'),
    path('profiles/',views.profiles,name='profiles'),
    path('register/',views.register,name='register'),
]