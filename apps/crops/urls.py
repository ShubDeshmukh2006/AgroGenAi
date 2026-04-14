from django.urls import path
from . import views

urlpatterns = [
    path('', views.crop_list, name='crop_list'),
    path('crop/<int:crop_id>/', views.crop_detail, name='crop_detail'),
]
