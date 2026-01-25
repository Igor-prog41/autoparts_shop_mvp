from django.shortcuts import render


def cart_view_http(request):

    return render(request, 'cart/cart.html', {

    })