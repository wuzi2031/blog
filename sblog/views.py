# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from sblog.models import *

# Create your views here.
def blog_list(request):
    # Author(name='wzm').save()
    a=Author.objects.last()
    # Blog(caption='测试1',author=a,content="dafadfsdfsfagf").save()
    blogs=Blog.objects.all()
    return render_to_response("blog_list.html",{'blogs':blogs})