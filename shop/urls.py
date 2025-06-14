from django.urls import path
from .views import Index, product_detail, comment_add, all_product_list, grid_display

app_name = 'shop'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('category/<slug:category_slug>/', Index.as_view(), name='products_by_category'),
    path('products/', all_product_list, name = 'products_list'),
    path('grid/', grid_display, name='grid'),
    path('detail/<int:product_id>/', product_detail, name='product_detail'),
    path('comment_add/<int:product_id>/', comment_add, name='comment_add'),
]