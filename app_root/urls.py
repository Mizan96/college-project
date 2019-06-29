"""app_root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static

from app_home.views import (index, staff, teacher, 
student, department, gallery, result, about, subject, excel_to_upload, submit_result)

urlpatterns = [
    url(r'^$', index, name='home'),
    url(r'^admin/', admin.site.urls),
    url(r'^staff/$', staff, name='staff'),
    url(r'^teacher/$', teacher, name='teacher'),
    url(r'^upload/(?P<url>[\w-]+)/$', excel_to_upload, name='excelToupload'),
    url(r'^student/$', student, name='student'),
    url(r'^department/$', department, name='department'),
    url(r'^(?P<id>[0-9]+)/$', subject, name='subject'),
    url(r'^gallery/$', gallery, name='gallery'),
    # url(r'^result/$', result, name='result'),
    url(r'^submitresult/$', submit_result, name='submitresult'),
    url(r'^result/(?P<roll>[0-9]+)$', result, name='result'),
    url(r'^about/$', about, name='about'),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + \
        static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + \
        static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
