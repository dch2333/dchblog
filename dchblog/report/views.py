from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import forms
from . import models
from django.template.loader import get_template
from datetime import date, datetime
from django.utils import timezone
# Create your views here.

'''
def showform(request):
    if request.session.get('is_login', None):
        template = get_template('report/report.html')
        form = models.Form.objects.all()
        now = timezone.now
        html = template.render(locals())
        return HttpResponse(html)
    else:
        return redirect('/login/')



        if request.method == 'POST':
            report_form = forms.ReportForm(request.POST)

            myclass = report_form.cleaned_data['myclass']
            name = report_form.cleaned_data['name']
            reason_in_school = report_form.cleaned_data['reason_in_school']
            reason_out_school = report_form.cleaned_data['reason_out_school']
            return_time = report_form.cleaned_data['return_time']
            tell = report_form.cleaned_data['tell']
            connect = report_form.cleaned_data['connect']
            another_tell = report_form.cleaned_data['another_tell']
            fudaoyuan = report_form.cleaned_data['fudaoyuan']

            new_form = models.Form()
            new_form.myclass = myclass
            new_form.name = name
            new_form.reason_in_school = reason_in_school
            new_form.reason_out_school = reason_out_school
            new_form.return_time = return_time
            new_form.tell = tell
            new_form.connect = connect
            new_form.another_tell = another_tell
            new_form.fudaoyuan = fudaoyuan
            new_form.save()
            return redirect('/report/')
        else:
            register_form = forms.RegisterForm()
            return render(request, 'report/report.html', locals())
'''


def showform(request):
    if request.session.get('is_login', None):
        template = get_template('report/report.html')
        form = models.Form.objects.all()
        now = timezone.now
        html = template.render(locals())

        if request.method == 'POST':
            report_form = forms.ReportForm(request.POST)

            myclass = report_form.cleaned_data['myclass']
            name = report_form.cleaned_data['name']
            reason_in_school = report_form.cleaned_data['reason_in_school']
            reason_out_school = report_form.cleaned_data['reason_out_school']
            return_time = report_form.cleaned_data['return_time']
            tell = report_form.cleaned_data['tell']
            connect = report_form.cleaned_data['connect']
            another_tell = report_form.cleaned_data['another_tell']
            fudaoyuan = report_form.cleaned_data['fudaoyuan']

            new_form = models.Form()
            new_form.myclass = myclass
            new_form.name = name
            new_form.reason_in_school = reason_in_school
            new_form.reason_out_school = reason_out_school
            new_form.return_time = return_time
            new_form.tell = tell
            new_form.connect = connect
            new_form.another_tell = another_tell
            new_form.fudaoyuan = fudaoyuan
            new_form.save()
            return HttpResponse(html)
        else:
            report_form = forms.ReportForm()
            return render(request, 'report/report.html', locals())

    else:
        return redirect('/login/')
