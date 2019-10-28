from django.contrib import admin
from .models import Customer, Size, Pizza, Ingredient, Order


@admin.register(Pizza)
class PizzaAdmin(admin.ModelAdmin):
    fields = (('name', 'ingredients'), 'size', 'price')
    list_display = ('name', 'size', 'price')
    ordering = ('name',)
    search_fields = ('name', 'price')
    list_filter = ('price',)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_vegan', 'is_meat')
    ordering = ('price',)
    list_filter = ('is_vegan', 'is_meat')


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'address', ('phone', 'email'))
    list_display = ('first_name', 'last_name', 'address','phone', 'email')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('date', 'customer', 'cost')


admin.site.register(Size)

