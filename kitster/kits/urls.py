from django.urls import path
from . import views

app_name = 'kits'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:kit_id>/', views.detail, name='detail'),
]