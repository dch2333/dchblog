from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.template.loader import get_template
from datetime import datetime
# Create your views here


def homepage(request):
    if request.session.get('is_login', None):
        template = get_template('index.html')
        posts = Post.objects.all()
        now = datetime.now()
        html = template.render(locals())
        return HttpResponse(html)
    else:
        return redirect('/login/')


def showpost(request, slug):
    if request.session.get('is_login', None):
        template = get_template('post.html')
        try:
            post = Post.objects.get(slug=slug)
            if post != None:
                now = datetime.now()
                html = template.render(locals())
                return HttpResponse(html)
        except:
            return redirect('/')
    else:
        return redirect('/login/')
