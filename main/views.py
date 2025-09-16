from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ShopForm
from main.models import Shop
from django.http import HttpResponse
from django.core import serializers
# Create your views here.

def show_main(request):
    shop_list = Shop.objects.all()
    context = {
        "nama_apps": "Exercise sport",
        "nama_ceo": "dery andreas",
        'umur': 'PBP D',
        'shop_list': shop_list
    }
    return render(request, "main.html", context)

def create_shop(request):
    if request.method == "POST":
        form = ShopForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ShopForm()
        return render(request, "create_shop.html", {"form": form})

def show_detail(request, shop_id):
    shop_item = get_object_or_404(Shop, pk=shop_id)
    return render(request, "detail_shop.html", {"shop_item": shop_item})

def show_xml(request):
     shop_list = Shop.objects.all()
     xml_data = serializers.serialize("xml", shop_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    shop_list = Shop.objects.all()
    json_data = serializers.serialize("json", shop_list)
    return HttpResponse(json_data, content_type="application/json")

def show_xml_by_id(request, shop_id):
   try:
       shop_item = Shop.objects.filter(pk=shop_id)
       xml_data = serializers.serialize("xml", shop_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, shop_id):
   try:
       shop_item = Shop.objects.get(pk=shop_id)
       json_data = serializers.serialize("json", [shop_item])
       return HttpResponse(json_data, content_type="application/json")
   except Shop.DoesNotExist:
       return HttpResponse(status=404)