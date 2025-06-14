from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from shop.models import Product, Category, Comment
from django.contrib import messages
from django.views.generic import ListView
from django.views import View
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.



class Index(View):
    def get(self, request, category_slug = None):
        search_query = request.GET.get('q', '')
        categories = Category.objects.all()

        if category_slug:
            products = Product.objects.filter(category__slug = category_slug)
            return render(request, 'shop/list.html', {'products': products})
        else:
            products = Product.objects.all()  # .order_by('price')

            if search_query:
                products = products.filter(name__icontains=search_query)

            paginator = Paginator(products, 2)
            page = request.GET.get('page')

            try:
                products = paginator.page(page)
            except PageNotAnInteger:
                products = paginator.page(1)
            except EmptyPage:
                products = paginator.page(paginator.num_pages)

            context = {'products': products, 'categories': categories}
            return render(request, 'shop/home.html', context)




def all_product_list(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/list.html', context)


def grid_display(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/grid.html', context)


def product_detail(request, product_id):
    try:
        products = Product.objects.get(id = product_id)
        context = {'product': products}
        return render(request, 'shop/detail.html', context)

    except products.DoesNotExist:
        return HttpResponse('Product not found')



def comment_add(request, product_id):
    product = get_object_or_404(Product, id = product_id)

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        content = request.POST.get('content')
        rating = request.POST.get('rating')

        if name and email and content and rating:
            Comment.objects.create(
                product=product,
                name=name,
                email=email,
                content=content,
                rating=rating
            )
            messages.success(request, "Comment successfully added")
        else:
            messages.error(request, "Invalid input")

        return redirect('shop:product_detail', product_id=product_id)

    return redirect('shop:product_detail', product_id=product.id)



