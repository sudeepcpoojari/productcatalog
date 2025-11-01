from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Product

class ProductListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        if query:
            products = Product.objects.filter(name__icontains=query)
        else:
            products = Product.objects.all()
        return render(request,'product_list.html', {'products': products, 'query': query})

class ProductCreateView(View):
    def get(self, request):
        return render(request,'add_product.html')

    def post(self, request):
        name = request.POST['name']
        price = request.POST['price']
        category = request.POST['category']
        Product.objects.create(name=name, price=price, category=category)
        return redirect('product_list')


# Create your views here.
