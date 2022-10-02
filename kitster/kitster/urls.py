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
from kits.views import index, maker, donate
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', index, name='index'),
    path('admin/', admin.site.urls),
    path('kits/', include('kits.urls')),
    path('agreement/', TemplateView.as_view(template_name='kits/agreement.html'), name='agreement'),
    path('<str:maker_name>/', maker, name='maker'),
    path('<str:maker_name>/donate/', donate, name='donate'),
]

print (urlpatterns)