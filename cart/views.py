from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from mainapp.models import Product
from .cart import Cart
from .forms import CartAddProductForm, CartAddProductFormMain
from django.contrib import messages


@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    form_main = CartAddProductFormMain(request.POST)
    if form_main.is_valid():
        cd = form_main.cleaned_data
        cart.add(product=product,
                 quantity=1,
                 update_quantity=cd['update'])
    messages.info(request, 'Товар "'+str(product)+'" добавлен в корзину')
    if request.POST['update'] == 'True':
        return redirect('cart:cart_detail')
    else:
        return redirect('/')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],
                                                                   'update': True})
    return render(request, 'cart/detail.html', {'cart': cart})