from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("quiz/subjects/<int:subject_id>/questions/<int:question_id>/", views.quiz ,name='quiz_question'),
]
