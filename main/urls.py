from django.urls import path
from main.views import show_main, show_xml, show_json, show_xml_by_id, show_json_by_id, create_shop, show_shop, add_shop_entry_ajax
from main.views import register
from main.views import login_user
from main.views import logout_user
from main.views import edit_shop
from main.views import delete_shop

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:shop_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:shop_id>/', show_json_by_id, name='show_json_by_id'),
    path('add/', create_shop, name='create_shop'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('shop/<uuid:id>/edit', edit_shop, name='edit_shop'),
    path('shop/<uuid:id>/delete', delete_shop, name='delete_shop'),
    path('shop/<str:id>/', show_shop, name='show_shop'),
    path('create-shop-ajax/', add_shop_entry_ajax, name='add_shop_entry_ajax'),

]
