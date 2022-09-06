from django.urls import path
from apps.chat import views

urlpatterns = [
    path('chat/', views.index, name='chatindex'),
]