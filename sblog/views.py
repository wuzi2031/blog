# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render_to_response
from sblog.models import *
from django.http import Http404
# Create your views here.
def blog_list(request):
    # Author(name='wzm').save()
    a=Author.objects.last()
    # Blog(caption='测试1',author=a,content="dafadfsdfsfagf").save()
    blogs=Blog.objects.all()
    return render_to_response("blog_list.html",{'blogs':blogs})

def blog_show(request,id=''):
    try:
        blog= Blog.objects.get(id=id)
    except Blog.DoesNotExist:
        raise Http404
    return render_to_response("blog_show.html",{"blog":blog})
def blog_filter(request, id=''):
    tags = Tag.objects.all()
    tag = Tag.objects.get(id=id)
    blogs = tag.blog_set.all()
    return render_to_response("blog_filter.html",
        {"blogs": blogs, "tag": tag, "tags": tags})