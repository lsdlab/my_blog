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
    File Name    : models.py
    Description  : define models for the core of this project
    Author       : Chen Jian
    Gmail        : lsdvincent@gmail.com
    GitHub       : http://github.com/lsdlab/my_blog
  -----------------------------------------------------------------------------
"""


from django.db import models


# Create your models here.
class Tag(models.Model):
    tag_name = models.CharField(max_length=64)

    def __unicode__(self):
        return self.tag_name


class Article(models.Model):
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    tag = models.ManyToManyField(Tag, blank=True)
    publish_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __unicode__(self):
        return self.title
