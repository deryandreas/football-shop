from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, create_shop, show_detail

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:shop_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:shop_id>/', show_json_by_id, name='show_json_by_id'),
    path('add/', create_shop, name='create_shop'),
    path('detail/<uuid:shop_id>/', show_detail, name='show_detail'),
]
