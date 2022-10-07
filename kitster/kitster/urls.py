"""kitster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from kits.views import index, maker, donate, profile
from django.views.generic.base import TemplateView
from django.contrib.sitemaps.views import sitemap
from django.contrib.sitemaps import GenericSitemap

from kits.models import Kit

info_dict = {
    'queryset': Kit.objects.all(),
    'date_field': 'pub_date',
}

sitemaps = {'kit': GenericSitemap(info_dict, priority=0.6)}

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('kits/', include('kits.urls')),
    path("robots.txt", TemplateView.as_view(template_name="site/robots.txt", content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('profile/', profile, name='profile'),
    path('agreement/', TemplateView.as_view(template_name='kits/agreement.html'), name='agreement'),
    path('<str:maker_name>/', maker, name='maker'),
    path('<str:maker_name>/donate/', donate, name='donate'),
]

handler404 = 'kits.views.handler404'
handler500 = 'kits.views.handler500'
