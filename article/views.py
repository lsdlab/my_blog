# -*- coding: utf-8 -*-

"""
  (c) Copyright BreakWire 2015 All Rights Reserved
  -----------------------------------------------------------------------------
  File Name    : views.py
  Description  : views functions for the app
  Author       : Chen Jian
  Gmail        : lsdvincent@gmail.com
  GitHub       : http://github.com/lsdlab/my_blog
  -----------------------------------------------------------------------------
"""


from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.http import Http404

# paginator import
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# RSS feed import  
from django.core.urlresolvers import reverse
from django.contrib.syndication.views import Feed

# models import 
from article.models import *


# Create your views here.
def home(request):
    posts = Article.objects.all().order_by('-publish_time')
    paginator = Paginator(posts, 3)
    page = request.GET.get('page')
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.paginator(paginator.num_pages)
    return render(request, 'home.html', {'post_list': post_list})


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        tags = post.tag.all()
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post': post, 'tags': tags})


def archives(request):
    try:
        post_list = Article.objects.all().order_by('-publish_time')
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'archives.html', {'post_list': post_list})


def category(request, category_filter):
    try:
        post_list = Article.objects.filter(category__iexact=category_filter)
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'category.html', {'post_list': post_list})


def about(request):
    return render(request, 'about.html')


def project(request):
    return render(request, 'project.html')


def resume(request):
    return render(request, 'resume.html')


class RSSFeed(Feed) :
    title = "陈坚的博客 RSS 订阅"
    link = "feed/post/"
    description = "陈坚的博客 RSS 订阅"

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