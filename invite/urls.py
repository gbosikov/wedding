from django.urls import path
from . import views

urlpatterns = [
    path('', views.invitation, name='invitation'),
    path('rsvp/', views.rsvp, name='rsvp'),  # опционально, если будем сохранять ответы
]