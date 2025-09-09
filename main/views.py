from django.shortcuts import render
from .models import Product   

def show_main(request):
    products = Product.objects.all()   
    context = {
        'app_name': 'Toko Olahraga BeliYuk',
        'npm': '2406425640',
        'name': 'Ganesha Taqwa',
        'class': 'PBP F',
        'products': products           
    }
    return render(request, "main.html", context)
