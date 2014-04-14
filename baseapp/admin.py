__author__ = 'Хедин'

from django.contrib import admin
from baseapp.models import History, Subusers, Linses, OrderProduct, Order, Product, AuthUser, Category, News, Cart



class ProductAdmin(admin.ModelAdmin):
    search_fields = ('category', 'product_name')
    list_display = ( 'product_name', 'category')

class SubusersAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name', 'date_of_birth', 'phone_number')
    search_fields = ('last_name', 'first_name', 'middle_name', 'date_of_birth')
#    search_fields = ('phone_number')

class HistoryAdmin(admin.ModelAdmin):
    list_display = ()

class LinsesAdmin(admin.ModelAdmin):
    list_display = ()

class OrderAdmin(admin.ModelAdmin):
    list_display = ()


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ()




admin.site.register(History)
#admin.site.register(Users)
admin.site.register(Subusers, SubusersAdmin)
admin.site.register(Linses)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(News)

