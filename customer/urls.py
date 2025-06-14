from django.urls import path

from shop.urls import urlpatterns
from .views import customer_list

app_name = 'customer'

urlpatterns = [
    path('', customer_list, name='customer_list'),
]