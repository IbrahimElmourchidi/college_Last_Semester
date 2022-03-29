from django.shortcuts import render
from .models import Product
# Create your views here.

def products_table(request):
    products_list = Product.objects.all()
    print(products_list[1])
    context = {
        "products":products_list
    }
    return render(request, 'products-table.html', context)