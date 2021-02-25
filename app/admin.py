from django.contrib.admin import ModelAdmin, StackedInline, TabularInline
from .models import *
from django.contrib import messages, auth, admin

@admin.register(Image)
class ImageAdmin(ModelAdmin):
	fields = ['id', 'name', 'img', 'width', 'height',  'url']
	list_display = ['id', 'name', 'width', 'height', 'url']
	readonly_fields = ['id', 'name', 'width', 'height',]
