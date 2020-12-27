from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'intro',
        'article',
        'image',
        'data_added',
    )


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
    )


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
