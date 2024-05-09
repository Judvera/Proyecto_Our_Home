from django.urls import path
from . import views
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('',views.indexView,name='home'),
    path('login/', LoginView.as_view(),name='login_url'),
    path('logout/', LogoutView.as_view(next_page='home'),name='logout'),
]