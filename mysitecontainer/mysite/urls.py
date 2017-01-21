"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from mysite.views import hello, hours_ahead, contact, thanks, basetesting, email, python, services, about, homepage
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'^hello/$', hello),
	url(r'^services/$', services),
	url(r'^home/$', homepage),
	url(r'^time/plus/(\d{1,2})/$', hours_ahead),
	url(r'^contact/$', contact),
	url(r'^contact/thanks/$', thanks),
	url(r'^$', homepage),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/home/'}, name='logout'),
    url(r'^admin/$', admin.site.urls),
    url(r'^testing/$', basetesting),
    url(r'^email/$', email),
    url(r'^python/$', python),
    url(r'^about/$', about),
]