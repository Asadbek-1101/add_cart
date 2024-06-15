from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, Cart
from .forms import CreateProduct
def home(request):
    products = Product.objects.filter(in_stock=True)
    categorys = Category.objects.all()
    return render(request, 'home.html', {"products":products, "cats":categorys})

def category(request, id):
    cat = get_object_or_404(Category, id=id)
    products = cat.products.all()
    categorys = Category.objects.all()
    return render(request, 'home.html', {"products": products, "cats":categorys})

def batafsil(request, id):
    product = get_object_or_404(Product, id=id)
    categorys = Category.objects.all()
    return render(request, 'batafsil.html', {"product": product, "cats": categorys})

def create_product(request):
    form = CreateProduct()
    if request.method == "POST":
        form = CreateProduct(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'create_product.html', {"form":form})

def update_product(request, id):
    product = get_object_or_404(Product, id=id)
    form = CreateProduct(instance=product)
    if request.method == "POST":
        form = CreateProduct(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('batafsil', id=product.id)
    return render(request, 'create_product.html', {"form": form})

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return redirect('/')

def add_cart(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST['cart'])
    cart = Cart()
    cart.product = product
    cart.quantity = quantity
    cart.save()
    return redirect('/')


