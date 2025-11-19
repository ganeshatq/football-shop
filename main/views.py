import datetime
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.db.models.functions import Cast
from django.db.models import CharField
from xml.etree.ElementTree import Element, SubElement, tostring
import requests
import json
from django.utils.html import strip_tags
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse
    
def proxy_image(request):
    image_url = request.GET.get('url')
    if not image_url:
        return HttpResponse('No URL provided', status=400)
    
    try:
        # Fetch image from external source
        response = requests.get(image_url, timeout=10)
        response.raise_for_status()
        
        # Return the image with proper content type
        return HttpResponse(
            response.content,
            content_type=response.headers.get('Content-Type', 'image/jpeg')
        )
    except requests.RequestException as e:
        return HttpResponse(f'Error fetching image: {str(e)}', status=500)

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get('filter', 'all')

    if (filter_type == 'all'):
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)
    context = {
        'appname' : 'Toko Olahraga BeliYuk',
        'name': 'Ganesha Taqwa',
        'class': 'PBP F',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never'),
    }

    return render(request, "main.html", context)

@login_required(login_url='/login')
def create_products(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        products_entry = form.save(commit=False)
        products_entry.user = request.user
        products_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_products.html", context)

@login_required(login_url='/login')
def show_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.increment_views()

    context = {
        'products': products
    }

    return render(request, "products_detail.html", context)

def edit_products(request, id):
    products = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=products)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_products.html", context)

def delete_products(request, id):
    products = get_object_or_404(Product, pk=id)
    products.delete()
    return HttpResponseRedirect(reverse("main:show_main"))

def show_xml(request):
    """
    Bangun XML manual dengan CAST id -> string supaya aman
    dari data UUID rusak.
    """
    qs = (Product.objects
          .annotate(id_text=Cast('id', output_field=CharField()))
          .values('id_text', 'name', 'price', 'description', 'category',
                  'thumbnail', 'products_views', 'created_at', 'is_featured', 'user_id'))

    root = Element('products')
    for row in qs:
        item = SubElement(root, 'product')

        SubElement(item, 'id').text = row['id_text']
        SubElement(item, 'name').text = row['name']
        SubElement(item, 'price').text = str(row['price'])
        SubElement(item, 'description').text = row['description']
        SubElement(item, 'category').text = row['category']
        SubElement(item, 'thumbnail').text = (row['thumbnail'] or "")
        SubElement(item, 'products_views').text = str(row['products_views'])
        SubElement(item, 'created_at').text = (row['created_at'].isoformat() if row['created_at'] else "")
        SubElement(item, 'is_featured').text = "true" if row['is_featured'] else "false"
        SubElement(item, 'user_id').text = (str(row['user_id']) if row['user_id'] is not None else "")

    xml_bytes = tostring(root, encoding='utf-8', method='xml')
    return HttpResponse(xml_bytes, content_type="application/xml")


def show_json(request):
    """
    JSON aman: CAST id -> string, ambil kolom yang perlu saja.
    """
    qs = (Product.objects
          .annotate(id_text=Cast('id', output_field=CharField()))
          .values('id_text', 'name', 'price', 'description', 'category',
                  'thumbnail', 'products_views', 'created_at', 'is_featured', 'user_id'))

    data = []
    for row in qs:
        data.append({
            'id': row['id_text'],
            'name': row['name'],
            'price': row['price'],
            'description': row['description'],
            'category': row['category'],
            'thumbnail': row['thumbnail'],
            'products_views': row['products_views'],
            'created_at': row['created_at'].isoformat() if row['created_at'] else None,
            'is_featured': row['is_featured'],
            'user_id': row['user_id'],
        })
    return JsonResponse(data, safe=False)

def show_xml_by_id(request, products_id):
    try:
        p = (Product.objects
             .filter(pk=products_id)
             .annotate(id_text=Cast('id', output_field=CharField()))
             .values('id_text', 'name', 'price', 'description', 'category',
                     'thumbnail', 'products_views', 'created_at', 'is_featured', 'user_id')
             .get())

        root = Element('products')
        item = SubElement(root, 'product')
        SubElement(item, 'id').text = p['id_text']
        SubElement(item, 'name').text = p['name']
        SubElement(item, 'price').text = str(p['price'])
        SubElement(item, 'description').text = p['description']
        SubElement(item, 'category').text = p['category']
        SubElement(item, 'thumbnail').text = (p['thumbnail'] or "")
        SubElement(item, 'products_views').text = str(p['products_views'])
        SubElement(item, 'created_at').text = (p['created_at'].isoformat() if p['created_at'] else "")
        SubElement(item, 'is_featured').text = "true" if p['is_featured'] else "false"
        SubElement(item, 'user_id').text = (str(p['user_id']) if p['user_id'] is not None else "")

        xml_bytes = tostring(root, encoding='utf-8', method='xml')
        return HttpResponse(xml_bytes, content_type="application/xml")
    except Product.DoesNotExist:
        return HttpResponse(status=404)

def show_json_by_id(request, products_id):
    try:
        p = (Product.objects
             .filter(pk=products_id)
             .annotate(id_text=Cast('id', output_field=CharField()))
             .values('id_text', 'name', 'price', 'description', 'category',
                     'thumbnail', 'products_views', 'created_at', 'is_featured', 'user_id')
             .get())

        data = {
            'id': p['id_text'],
            'name': p['name'],
            'price': p['price'],
            'description': p['description'],
            'category': p['category'],
            'thumbnail': p['thumbnail'],
            'products_views': p['products_views'],
            'created_at': p['created_at'].isoformat() if p['created_at'] else None,
            'is_featured': p['is_featured'],
            'user_id': p['user_id'],
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

# ============================================================

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

    else:
        form = AuthenticationForm(request)
    context = {'form': form}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@csrf_exempt
@require_POST
def add_products_entry_ajax(request):
    """
    Perbaiki nama field: sebelumnya pakai 'title' dan 'content',
    padahal di model/form: 'name' dan 'description'.
    Juga pastikan 'price' jadi int.
    """
    name = request.POST.get("name")
    price_raw = request.POST.get("price")
    description = request.POST.get("description")
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured_val = request.POST.get("is_featured")  # 'on' / 'true' / '1'
    is_featured = str(is_featured_val).lower() in ('on', 'true', '1', 'yes')
    user = request.user if request.user.is_authenticated else None

    try:
        price = int(price_raw) if price_raw is not None else 0
    except ValueError:
        price = 0

    new_products = Product(
        name=name,
        price=price,
        description=description or "",
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user
    )
    new_products.save()
    return HttpResponse(b"CREATED", status=201)

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        name = strip_tags(data.get("name", ""))  # Strip HTML tags
        price = data.get("price", 0)
        description = strip_tags(data.get("description", ""))  # Strip HTML tags
        category = data.get("category", "")
        thumbnail = data.get("thumbnail", "")
        is_featured = data.get("is_featured", False)
        user = request.user if request.user.is_authenticated else None

        try:
            price = int(price)
        except ValueError:
            price = 0

        new_product = Product(
            name=name,
            price=price,
            description=description,
            category=category,
            thumbnail=thumbnail,
            is_featured=is_featured,
            user=user
        )
        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)
