from django.urls import path

from . import views

app_name = 'portfolio'

urlpatterns = [
    path('', views.index, name='index'),
    path('portfolio/list/', views.list, name='list'),
    path('portfolio/detail/<int:detail_id>', views.detail, name='detail'),
]