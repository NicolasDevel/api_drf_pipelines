from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.list_products, name="lista_productos"),
    path('products/store', views.store_product, name="guardar_producto"),
    path('products/<int:product_id>', views.detail_product, name="ver_actualizar_borrar_productos")
]
