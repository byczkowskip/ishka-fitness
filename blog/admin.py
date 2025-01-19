from django.contrib import admin
from blog import models


@admin.register(models.Category)
class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_active', 'created_at', 'updated_at']
    search_fields = ['name']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(models.Post)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at', 'updated_at']
    search_fields = ['title', 'category__name']
    prepopulated_fields = {'slug': ('title',)}
