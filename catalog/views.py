from django.shortcuts import render
from django.views import View
from django.shortcuts import redirect
from .models import Product

class ProductListView(View):
    def get(self, request):
        query = request.GET.get('q', '')
        sort_by = request.GET.get('sort_by', 'id')
        order = request.GET.get('order', 'asc')

        products = Product.objects.all()

        if query:
            products = products.filter(name__icontains=query)

        if request.GET.get('sort_by'):  # Only apply sorting if sort form used
            if order == 'desc':
                sort_by = '-' + sort_by
            products = products.order_by(sort_by)

        return render(request, 'product_list.html', {
            'products': products,
            'query': query,
            'sort_by': sort_by.lstrip('-'),
            'order': order,
        })



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
