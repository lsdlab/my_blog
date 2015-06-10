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
    File Name    : views.py
    Description  : views functions for the app
    Author       : Chen Jian
    Gmail        : lsdvincent@gmail.com
    GitHub       : http://github.com/lsdlab/my_blog
    ---------------------------------------------------------------------------
"""


from django.shortcuts import render
from django.http import Http404

# paginator import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# RSS feed import  
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed

# models import 
from article.models import *


# Create your views here.
# home tab
def home(request):
    posts = Article.objects.all().order_by('-publish_time')
    paginator = Paginator(posts, 6)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


# each post
def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = post.tag.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'tags': tags})


# archives tab
def archives(request):
    try:
        post_list = Article.objects.all().order_by('-publish_time')
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list})


# category
def category(request, category_filter):
    try:
        post_list = Article.objects.filter(category__iexact=category_filter)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'category.html', {'post_list': post_list})


# about tab
def about(request):
    return render(request, 'about.html')


# project tab
def project(request):
    return render(request, 'project.html')


# resume tab
def resume(request):
    return render(request, 'resume.html')


# RSS Subscription
class RSSFeed(Feed) :
    title = "BreakWire RSS Subscription"
    link = "feed/post/"
    description = "BreakWire RSS Subscription"

    def items(self):
        return Article.objects.order_by('-publish_time')[:3]

    def item_title(self, item):
        return item.title

    def item_pubdate(self, item):
        return item.publish_time

    def item_description(self, item):
        return item.content
    
    def item_link(self, item):
        return reverse('detail', args=[item.id])