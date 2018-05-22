from django.contrib import admin
from .models import Article, Editor, Tags


class ArticleAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

# Register your models here.
admin.site.register(Article, ArticleAdmin)
admin.site.register(Editor)
admin.site.register(Tags)
