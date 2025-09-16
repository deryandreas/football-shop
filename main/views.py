from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm
from main.models import Shop
from django.http import HttpResponse
from django.core import serializers

# Halaman utama
def show_main(request):
    shop_list = Shop.objects.all()
    context = {
        "nama_apps": "Exercise sport",
        "nama_ceo": "dery andreas",
        "umur": "PBP D",
        "shop_list": shop_list
    }
    return render(request, "main.html", context)

# Form tambah shop
def create_shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("main:show_main")
    else:
        form = ShopForm()
    return render(request, "create_shop.html", {"form": form})

# Detail shop (pakai UUID)
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
