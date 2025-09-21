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
        'name': "Dery Andreas Tampubolon",
        'class': 'PBP D',
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

# Detail shop (pakai UUID)
@login_required(login_url='/login')
def show_detail(request, shop_id):
    shop_item = get_object_or_404(Shop, pk=shop_id)
    shop_item.increment_views()  # contoh: nambah views
    return render(request, "detail_shop.html", {"shop_item": shop_item})

# Semua data XML
def show_xml(request):
    shop_list = Shop.objects.all()
    xml_data = serializers.serialize("xml", shop_list)
    return HttpResponse(xml_data, content_type="application/xml")

# Semua data JSON
def show_json(request):
    shop_list = Shop.objects.all()
    json_data = serializers.serialize("json", shop_list)
    return HttpResponse(json_data, content_type="application/json")

# Data berdasarkan UUID (XML)
def show_xml_by_id(request, shop_id):
    shop_item = get_object_or_404(Shop, pk=shop_id)
    xml_data = serializers.serialize("xml", [shop_item])
    return HttpResponse(xml_data, content_type="application/xml")

# Data berdasarkan UUID (JSON)
def show_json_by_id(request, shop_id):
    shop_item = get_object_or_404(Shop, pk=shop_id)
    json_data = serializers.serialize("json", [shop_item])
    return HttpResponse(json_data, content_type="application/json")

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