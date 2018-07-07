from django.shortcuts import render
from django.shortcuts import redirect
from . import forms
from . import models
from datetime import datetime
# Create your views here.


def login(request):
    if request.session.get('is_login', None):
        return redirect('/')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '所有的字段都必须填写！'
        if login_form.is_valid():
            name = login_form.cleaned_data.get('name')
            password = login_form.cleaned_data.get('password')
            # ....
            try:
                user = models.User.objects.get(name=name)
            except:
                message = '用户不存在'
                return render(request, 'login/login.html', locals())

            if password == user.password:
                request.session['is_login'] = True
                request.session['user_name'] = user.name
                return redirect('/')
            else:
                message = '密码错误'
                return render(request, 'login/login.html', locals())
        else:
            return render(request, 'login/login.html', locals())

    login_form = forms.UserForm()
    return render(request, 'login/login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/')

    if request.method == "POST":
        register_form = forms.RegisterForm(request.POST)
        message = '请检查填写的内容!'
        if register_form.is_valid():
            name = register_form.cleaned_data['name']
            password1 = register_form.cleaned_data['password1']
            password2 = register_form.cleaned_data['password2']
            email = register_form.cleaned_data['email']
            if password1 != password2:
                message = '两次输入的密码不相同！'
                return render(request, 'login/register.html', locals())
            else:
                same_name_user = models.User.objects.filter(name=name)
                if same_name_user:
                    message = '用户名已经存在，请重新选择！'
                    return render(request, 'login/register.html', locals())
                same_email_user = models.User.objects.filter(email=email)
                if same_email_user:
                    message = '该邮箱地址已经被注册，请使用别的邮箱！'
                    return render(request, 'login/register.html', locals())

            new_user = models.User()
            new_user.name = name
            new_user.password = password2
            new_user.email = email
            new_user.save()

            return redirect('/login/')
    register_form = forms.RegisterForm()
    return render(request, 'login/register.html', locals())


def logout(request):
    if not request.session.get('is_login', None):
        return redirect("/")
    request.session.flush()
    return redirect("/")
