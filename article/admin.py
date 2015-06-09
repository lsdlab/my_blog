# -*- coding: utf-8 -*-

"""
     _____  _   _   ____  _  __
    |  ___|| | | | / ___|| |/ /
    | |_   | | | || |    | ' / 
    |  _|  | |_| || |___ | . \ 
    |_|     \___/  \____||_|\_\
                               
     _____ __     __ _____  ____ __   __ ____    ___   ____ __   __
    | ____|\ \   / /| ____||  _ \\ \ / /| __ )  / _ \ |  _ \\ \ / /
    |  _|   \ \ / / |  _|  | |_) |\ V / |  _ \ | | | || | | |\ V / 
    | |___   \ V /  | |___ |  _ <  | |  | |_) || |_| || |_| | | |  
    |_____|   \_/   |_____||_| \_\ |_|  |____/  \___/ |____/  |_|  

    (c) Copyright BreakWire 2015 All Rights Reserved
    ---------------------------------------------------------------------------
    File Name    : admin.py
    Description  : admin customise settings
    Author       : Chen Jian
    Gmail        : lsdvincent@gmail.com
    GitHub       : http://github.com/lsdlab/my_blog
  -----------------------------------------------------------------------------
"""


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
