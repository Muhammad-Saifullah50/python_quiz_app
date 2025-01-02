
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.getSubjects)
]