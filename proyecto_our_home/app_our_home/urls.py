from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile

urlpatterns = [
    path('',views.indexView,name='home'),
    path('login/', LoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='home'),name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
]