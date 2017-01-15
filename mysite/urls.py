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
from moment import views as moment_views

urlpatterns = [
	url(r'^moment/public.html', moment_views.public),
	url(r'^moment/add_word_public', moment_views.add_word_public),
    #url(r'^moment/private.html', moment_views.private),
    #url(r'^moment/add_word_private', moment_views.add_word_private),
    url(r'^admin/', admin.site.urls),
]
