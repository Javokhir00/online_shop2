from django.urls import path
from .views import login_page, register, logout

app_name = 'users'

urlpatterns = [
    path('' , register , name='register'),
    path('login/' , login_page , name='login'),
    path('register/' , register , name='register'),
    path('logout/' , logout , name='logout'),

]