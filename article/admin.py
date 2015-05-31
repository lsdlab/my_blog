from django.contrib import admin
from article.models import *


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'publish_time')
    search_fields = (
        'title', 'category', 'tag', 'publish_time', 'update_time' 'content')
    list_filter = ('publish_time',)
    date_hierarchy = 'publish_time'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Tag)
