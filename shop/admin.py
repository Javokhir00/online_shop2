from django.contrib import admin
from django.contrib.auth.models import User, Group
from shop.models import Category, Product, ProductImage, Comment, AttributeKey, AttributeValue, Attribute
# from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(Category)
# admin.site.register(Product)
admin.site.register(Comment)


# admin.site.unregister(User)
admin.site.unregister(Group)



class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'avg_rating')
    list_filter = ('category', 'price', 'created_at')
    inlines = [ProductImageInline]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'slug']

    prepopulated_fields = {'slug': ('title',)}


admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(Attribute)


admin.site.site_header = 'Admin'
admin.site.site_title = 'Admin'
admin.site.index_title = 'Welcome to Shop Admin'
