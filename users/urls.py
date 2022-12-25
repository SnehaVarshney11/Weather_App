from django.urls import path
from . import views
from django.contrib.auth import views as auth_view 
# here we are importing all the Views from the views.py file
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('ind/', views.index, name='ind'),
    path('weatherupdates/', views.showweatherapp, name='showweatherapp'),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_view.LogoutView.as_view(template_name='users/logout.html'), name="logout")  
]
