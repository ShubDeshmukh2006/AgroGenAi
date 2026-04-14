from django.urls import path
from . import views

urlpatterns = [
    path('', views.unified_assistant, name='unified_assistant'),
    path('chat/', views.chat_with_ai, name='chat_with_ai'),
]
