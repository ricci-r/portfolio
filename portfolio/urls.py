from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/', views.list, name='list'),
    path('portfolio/<slug:slug>', views.detail, name='detail'),
]