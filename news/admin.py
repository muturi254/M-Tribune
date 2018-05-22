from django.contrib import admin
from .models import Article, Editor, Tags

class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('Tags')

# Register your models here.
admin.site.register(Article)
admin.site.register(Editor)
admin.site.register(Tags)