from django.urls import path
from . import views

app_name = 'kits'

urlpatterns = [
    path('<int:kit_id>/', views.detail, name='detail'),
]