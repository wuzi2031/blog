# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from sblog.models import *

# Create your views here.
def blog_list(request):
    a=Author(name='wzm').save()
    Blog(caption='测试1',author=a,content="dafadfsdfsfagf").save()
    blogs=Blog.objects.all()
    return render("blog_list.html",{blogs:blogs})