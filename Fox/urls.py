"""
URL configuration for Fox project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from FoxApp.views import *
from Fox import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('post/<str:id>',post,name='post'),
    path('subscribe/',subscribe,name='subscribe'),
    path('blog/',blog,name='blog'),
    path('portfolio/',portfolio,name='portfolio'),
    path('projet/<str:id>',projet,name='projet'),
    path('success/<str:message>',success,name='success'),
    path('comment/<str:id>',comment,name='comment'),
    path('sendNews/', send_newsletter, name='sendNews'),
    path('sendMessage/', sendMessage, name='sendMessage'),

              ]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
