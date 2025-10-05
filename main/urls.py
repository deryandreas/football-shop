# main/urls.py
from django.urls import path
from . import views 
from uuid import UUID # Diperlukan untuk <uuid:id>

app_name = 'main'

urlpatterns = [
    # --- URL TAMPILAN UTAMA & DATA FEED ---
    path('', views.show_main, name='show_main'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<uuid:shop_id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:shop_id>/', views.show_json_by_id, name='show_json_by_id'),
    
    # --- URL CRUD MANUAL ---
    path('add/', views.create_shop, name='create_shop'),
    path('shop/<str:id>/', views.show_shop, name='show_shop'),
    path('shop/<uuid:id>/edit', views.edit_shop, name='edit_shop'),
    path('shop/<uuid:id>/delete', views.delete_shop, name='delete_shop'),

    # --- URL AUTHENTICATION MANUAL ---
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),

    
    # 1. CREATE AJAX (Nama Baru)
    path('create-ajax/', views.create_shop_ajax, name='create_shop_ajax'), 

    # 2. CREATE AJAX (Nama Lama untuk kompatibilitas)
    path('add-entry-ajax/', views.create_shop_ajax, name='add_shop_entry_ajax'), 
    
    # UPDATE AJAX
    path('edit-ajax/<uuid:id>/', views.edit_shop_ajax, name='edit_shop_ajax'),
    
    # DELETE AJAX
    path('delete-ajax/<uuid:id>/', views.delete_shop_ajax, name='delete_shop_ajax'),
    
 
    path('login-ajax/', views.login_user_ajax, name='login_ajax'),
    path('register-user-ajax/', views.register_user_ajax, name='register_user_ajax'), 
    path('logout-ajax/', views.logout_user_ajax, name='logout_ajax'),
]