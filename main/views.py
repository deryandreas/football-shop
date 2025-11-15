from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm
from main.models import Shop
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.http import HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
from django.views.decorators.http import require_http_methods 
import json
import requests
from django.views.decorators.csrf import csrf_exempt
from django.utils.html import strip_tags
import json
from django.http import JsonResponse

# Halaman utama

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'
    sort_order = request.GET.get("sort")

    if filter_type == "all":
        shop_list = Shop.objects.all()
    else:
        shop_list = Shop.objects.filter(user=request.user)


    if sort_order == "price-asc":
        shop_list = shop_list.order_by("price")
    elif sort_order == "price-desc":
        shop_list = shop_list.order_by("price")

    if request.headers.get('x-request-with') == 'XMLHttpRequest':
        data = list(shop_list.values('name', 'price', 'description'))
        return JsonResponse(data, safe=False)

    context = {
        'npm': '2406347380',
        'nama_apps': 'Exercise Sport',
        'nama_ceo': "Dery Andreas Tampubolon",
        'class': 'PBP D',
        'umur': 19,
        'shop_list': shop_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }
    return render(request, "main.html",context)


# Form tambah shop
def create_shop(request):
    form = ShopForm(request.POST or None)

    if form.is_valid() and request.method == 'POST':
        shop_entry = form.save(commit = False)
        shop_entry.user = request.user
        shop_entry.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "create_shop.html", context)


@login_required(login_url='/login')
def show_shop(request, id):
    shop = get_object_or_404(Shop, pk=id)
    shop.increment_views()

    context = {
        'shop': shop
    }

    return render(request, "detail_shop.html", context)

# Semua data XML
def show_xml(request):
    shop_list = Shop.objects.all()
    xml_data = serializers.serialize("xml", shop_list)
    return HttpResponse(xml_data, content_type="application/xml")

# Semua data JSON
def show_json(request):
    shop_list = Shop.objects.all()
    data = [
        {
            'id': str(shop.id),
            'name': shop.name,
            'price': shop.price,
            'description': shop.description,
            'thumbnail': shop.thumbnail,
            'category': shop.category,
            'is_featured': shop.is_featured,
            'stok': shop.stok,
            'product_views': shop.product_views,
            'user': shop.user.username if shop.user else None,
            
            # PENTING: Mengirim ID pemilik dengan nama user_owner_id (untuk JS)
            'user_owner_id': shop.user.id if shop.user else None, 
            
            'diskon': shop.diskon,
            # PERBAIKAN DATE: Mengirim tanggal dalam format ISO 8601 yang dapat dibaca JS
            'created_at': shop.created_at.isoformat() if shop.created_at else None, 
        }
        for shop in shop_list
    ]
    return JsonResponse(data, safe=False)

# Data berdasarkan UUID (XML)
def show_xml_by_id(request, shop_id):
    shop_item = get_object_or_404(Shop, pk=shop_id)
    xml_data = serializers.serialize("xml", [shop_item])
    return HttpResponse(xml_data, content_type="application/xml")

# Data berdasarkan UUID (JSON)
def show_json_by_id(request, shop_id):
    try:
        shop = Shop.objects.select_related('user').get(pk=shop_id)
        data = {
           'id': str(shop.id),
            'name': shop.name,
            'price': shop.price,
            'description': shop.description,
            'thumbnail': shop.thumbnail,
            'category': shop.category,
            'is_featured': shop.is_featured,
            'stok': shop.stok,
            'product_views': shop.product_views,
            'user_id': shop.user.id if shop.user else None,  # <-- aman
            'diskon': shop.diskon,
            'created_at': shop.created_at.isoformat() if hasattr(shop, 'created_at') else None,
            'user_username': shop.user.username if shop.user_id else None,

        }
        return JsonResponse(data)
    except Shop.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)

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

def edit_shop(request, id):
    shop = get_object_or_404(Shop, pk=id)
    form = ShopForm(request.POST or None, instance=shop)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_shop.html", context)

def delete_shop(request, id):
    shop = get_object_or_404(Shop, pk=id)
    shop.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

@csrf_exempt
@require_http_methods(["POST"])
def create_shop_ajax(request):
    if not request.user.is_authenticated:
        return JsonResponse({'status': 'error', 'message': 'Authentication required'}, status=403)
        
    try:
        # PENTING: BACA DATA DARI BODY SEBAGAI JSON (MENGATASI "None")
        data = json.loads(request.body)
        
        new_shop = Shop.objects.create(
            user=request.user, # Field Anda bernama 'user'
            name=data.get('name', 'Product Name'), 
            description=data.get('description', 'No Description'),
            price=data.get('price', 0),    
            stok=data.get('stok', 0),
            category=data.get('category'),
            thumbnail=data.get('thumbnail'),
            is_featured=data.get('is_featured', False),
            diskon=data.get('diskon', 0)
        )
        
        return JsonResponse({"status": "success", "message": "Shop created successfully"}, status=201)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': f'Server error: {str(e)}'}, status=400)

@csrf_exempt
@require_http_methods(["PUT"])
def edit_shop_ajax(request, id):
    shop = get_object_or_404(Shop, pk=id)

    if shop.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Not authorized'}, status=403)
        
    try:
        data = json.loads(request.body)
        
        # UPDATE FIELD
        shop.name = data.get('name', shop.name)
        shop.description = data.get('description', shop.description)
        shop.price = data.get('price', shop.price)
        shop.stok = data.get('stok', shop.stok)
        shop.category = data.get('category', shop.category)
        shop.thumbnail = data.get('thumbnail', shop.thumbnail)
        shop.is_featured = data.get('is_featured', shop.is_featured)
        shop.diskon = data.get('diskon', shop.diskon)
        
        shop.save()
        
        return JsonResponse({'status': 'success', 'message': 'Shop updated successfully'}, status=200)

    except Exception as e:
        return JsonResponse({'status': 'error', 'message': str(e)}, status=400)


@csrf_exempt
@require_http_methods(["DELETE"])
def delete_shop_ajax(request, id):
    shop = get_object_or_404(Shop, pk=id)
    
    if shop.user != request.user:
        return JsonResponse({'status': 'error', 'message': 'Not authorized'}, status=403)
        
    shop.delete()
    return JsonResponse({'status': 'success', 'message': 'Shop deleted successfully'}, status=204)

@csrf_exempt
@require_http_methods(["POST"])
def login_user_ajax(request):
    data = json.loads(request.body)
    username = data.get('username')
    password = data.get('password')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        # Mengembalikan data untuk diolah di frontend (untuk Toast/Update Navbar)
        return JsonResponse({"status": "success", "message": "Login successful", "username": username}, status=200)
    else:
        return JsonResponse({"status": "error", "message": "Invalid credentials"}, status=401)

@csrf_exempt
@require_http_methods(["POST"])
def register_user_ajax(request):
    # Debug log untuk lihat isi request
    print("REQUEST BODY RAW:", request.body)

    try:
        data = json.loads(request.body)
        print("PARSED JSON:", data)
    except json.JSONDecodeError:
        return JsonResponse({
            "status": "error",
            "message": "Invalid JSON format."
        }, status=400)

    # Buat form dengan field sesuai UserCreationForm
    form = UserCreationForm({
        'username': data.get('username', ''),
        'password1': data.get('password1', ''),
        'password2': data.get('password2', ''),
    })

    if form.is_valid():
        user = form.save()
        return JsonResponse({
            "status": "success",
            "message": "Account created successfully!",
            "username": user.username
        }, status=201)
    else:
        errors = dict(form.errors.items())
        print("FORM ERRORS:", errors)  # tambahan debug
        return JsonResponse({
            "status": "error",
            "message": "Registration failed.",
            "errors": errors
        }, status=400)
        
@csrf_exempt
@require_http_methods(["POST"])
def logout_user_ajax(request):
    logout(request)
    return JsonResponse({"status": "success", "message": "Logged out successfully"}, status=200)

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
    
@csrf_exempt
def create_shop_flutter(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        name = strip_tags(data.get("name", ""))
        price = data.get("price", 0)
        description = strip_tags(data.get("description", ""))
        thumbnail = data.get("thumbnail", "")
        category = data.get("category", "")
        is_featured = data.get("is_featured", False)
        stok = data.get("stok", 0)
        diskon = data.get("diskon", 0)

        # otomatis: product_views = 0
        product_views = 0  

        # user dari session login
        user = request.user if request.user.is_authenticated else None

        new_shop = Shop(
            name=name,
            price=price,
            description=description,
            thumbnail=thumbnail,
            category=category,
            isFeatured=is_featured,
            stok=stok,
            productViews=product_views,
            user=user.username if user else None,
            userOwnerId=user.id if user else None,
            diskon=diskon,
            createdAt=datetime.timezone.now()
        )

        new_shop.save()

        return JsonResponse({"status": "success"}, status=200)

    return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)
