#!/usr/bin/python2.7
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.core.mail import send_mail
from mysite.forms import ContactForm
import datetime
from employees.models import employees
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.conf import settings
import os


from urlparse import urlparse
from twilio.rest.resources import Connection
from twilio.rest.resources.connection import PROXY_TYPE_HTTP

proxy_url = os.environ.get("http_proxy")
host, port = urlparse(proxy_url).netloc.split(":")
Connection.set_proxy_info(host, int(port), proxy_type=PROXY_TYPE_HTTP)

import twilio
import twilio.rest

def hello(request):
    return HttpResponse("Hello world")

def thanks(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('//')
    else:
        return render(request, 'thanks.html')


def homepage(request):
    now = datetime.datetime.now()
    return render(request, 'home.html', {'current_date': now})

def about(request):
    now = datetime.datetime.now()
    return render(request, 'about.html', {'current_date': now})

def email(request):
    return render(request, 'email.html')

def python(request):
    return render(request, 'python.html')

def basetesting(request):
    return render(request, 'basetesting.html')

def excel(request):
    now = datetime.datetime.now()
    return render(request, 'excel.html', {'current_date': now})
def services(request):
    now = datetime.datetime.now()
    return render(request, 'services.html', {'current_date': now})

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render(request, 'hours_ahead.html', {'hour_offset':offset,'next_time': dt})
    #return HttpResponse(html)
'''
def contactexisiting(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                for to_groups in cd['togroup']:
                    recipients = employees.objects.filter(group=to_groups)
                    client = twilio.rest.TwilioRestClient('AC71641f236c273d84e7d1d570370b53ac', '7f648ae24da547ad0b7e159bcbe9596d')
                    for recipient in recipients:
                        client.messages.create(body=cd['message'], to=recipient.phone_number, from_='+19733595858')

                return HttpResponseRedirect('/contact/thanks/')
'''
def contact(request):
    if not request.user.is_authenticated():
        return HttpResponseRedirect('/login/')
    else:
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                #sel_groups = request.POST.getlist('togroup')
                for to_groups in cd['togroup']:
                    recipients = employees.objects.filter(group=to_groups)
                    with open('/home/mnoah66/mysitecontainer/mysite/twiliosid.txt') as f:
                        sid = f.read().strip()
                    with open('/home/mnoah66/mysitecontainer/mysite/twilioauth.txt') as f:
                        key = f.read().strip()

                    client = twilio.rest.TwilioRestClient(sid, key)
                    for recipient in recipients:
                        client.messages.create(body=cd['message'], to=recipient.phone_number, from_='+19733595858')
                    if cd['yourname']:
                        client.messages.create(body=cd['message'], to=cd['yourname'], from_='+19733595858')

                return HttpResponseRedirect('/contact/thanks/')

        else:
            form = ContactForm(initial={'message': 'Enter message here...'})
        now = datetime.datetime.now()
        return render(request, 'newcontactform.html', {'form':form,'current_date': now})