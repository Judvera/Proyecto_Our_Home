from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from .views import register, profile, login_view

urlpatterns = [
    path('',views.indexView,name='home'),
    path('login/', login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='home'),name='logout'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    
    path('add_property/', views.add_property, name='add_property'),
    path('update_property/<int:property_id>/', views.update_property, name='update_property'),
    path('delete_property/<int:property_id>/', views.delete_property, name='delete_property'),
    # path('property/', views.property_list, name='property_list'),
    path('property_list/', views.property_list, name='property_list'),
]