from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, login_view, logout_view, add_property, delete_property, property_list, landlord_property, update_property

urlpatterns = [
    path('',views.indexView,name='home'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('landlord_property/', landlord_property, name='landlord_property'),
    path('add_property/', add_property, name='add_property'),
    path('update_property/<int:property_id>/', update_property, name='update_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    path('property_list/', property_list, name='property_list'),
]