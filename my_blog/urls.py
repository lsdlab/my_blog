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
  -----------------------------------------------------------------------------
  File Name    : urls.py
  Description  : url config for the app
  Author       : Chen Jian
  Gmail        : lsdvincent@gmail.com
  GitHub       : http://github.com/lsdlab/my_blog
  -----------------------------------------------------------------------------
"""


from django.conf.urls import patterns, include, url
from django.contrib import admin

# RSS import
from article.views import RSSFeed

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'my_blog.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^$', "article.views.home", name='home'),
                       url(r'^(?P<id>\d+)/$',
                           'article.views.detail', name='detail'),
                       url(r'^archives/$', 'article.views.archives',
                           name='archives'),
                       url(r'^category/(?P<category_filter>\w+)/$',
                           'article.views.category', name='category'),
                       url(r'^about/$', 'article.views.about', name='about'),
                       url(r'^project/$', 'article.views.project', name='project'),
                       url(r'^resume/$', 'article.views.resume', name='resume'),
                       url(r'^feed/$', RSSFeed(), name='RSS'),
                       )
