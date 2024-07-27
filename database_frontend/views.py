from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from .models import Product

@cache_page(60 * 15)
def product_list(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})
