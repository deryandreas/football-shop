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



# Halaman utama

@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        shop_list = Shop.objects.all()
    else:
        shop_list = Shop.objects.filter(user=request.user)

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
            'user': shop.user.username if shop.user else None,  # <-- aman
            'user_id': shop.user.id if shop.user else None, 
            'diskon': shop.diskon,
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
@require_POST
def add_shop_entry_ajax(request):
    name = strip_tags(request.POST.get("title")) # strip HTML tags!
    content = strip_tags(request.POST.get("content")) # strip HTML tags!
    category = request.POST.get("category")
    thumbnail = request.POST.get("thumbnail")
    is_featured = request.POST.get("is_featured") == 'on'  # checkbox handling
    user = request.user
    price = request.POST.get("price", 0) 
    stok = request.POST.get("stok", 0) 

    new_shop = Shop(
        name=name, 
        description=content,
        category=category,
        thumbnail=thumbnail,
        is_featured=is_featured,
        user=user,
        price=price,        
        stok=stok,  
    )
    new_shop.save()

    return HttpResponse(b"CREATED", status=201)