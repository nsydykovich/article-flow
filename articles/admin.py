from django.contrib import admin
from .models import Article

# Register your models here.
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    fields = ["title", "description", "content"]
    ordering = ("title", "description", "content")
    list_display = ["title", "description"]
