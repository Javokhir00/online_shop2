from django.urls import path
from .views import index, product_detail, comment_add

app_name = 'shop'

urlpatterns = [
    path('', index, name='index'),
    path('category/<int:category_id>/', index, name='products_by_category'),
    path('detail/<int:product_id>/', product_detail, name='product_detail'),
    path('comment_add/<int:product_id>/', comment_add, name='comment_add'),
]