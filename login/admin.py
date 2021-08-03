from django.contrib import admin
from .models import Profile, Products



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('id','firstname','lastname','email','phone_no','address','shipping_address')

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display=('productname','productdescription','productprice','productimage')