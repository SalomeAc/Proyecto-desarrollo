from django.contrib import admin
from productos.models import Producto


class ProductosAdmin(admin.ModelAdmin):
    list_display = ("nombre", "categoria", "precio")
    list_filter = ("categoria",)
    search_fields = ("nombre", "categoria", "precio")



admin.site.register(Producto, ProductosAdmin)




