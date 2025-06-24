from django.urls import path

from shop.urls import urlpatterns
from .views import customer_list, send_email

app_name = 'customer'

urlpatterns = [
    path('', customer_list, name='customer_list'),
    path('send_email/', send_email, name = 'send_email'),
]


