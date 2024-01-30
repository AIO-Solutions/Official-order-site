from django.contrib import admin

# Register your models here.
from .models import About

@admin.register(About)
class EddAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','linkedin','instagram']
    search_fields = ['pk','first_name']
