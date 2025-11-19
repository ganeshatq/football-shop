from django.urls import path
from main.views import show_main, create_products, show_products, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_products, delete_products, add_products_entry_ajax, proxy_image, create_product_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-products/', create_products, name='create_products'),
    path('products/<uuid:id>/', show_products, name='show_products'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<uuid:products_id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<uuid:products_id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/<uuid:id>/edit', edit_products, name='edit_products'),
    path('products/<uuid:id>/delete', delete_products, name='delete_products'),
    path('create-products-ajax', add_products_entry_ajax, name='add_products_entry_ajax'),
    path('proxy-image/', proxy_image, name='proxy_image'),
    path('create-product-flutter/', create_product_flutter, name='create_product_flutter'),
]
