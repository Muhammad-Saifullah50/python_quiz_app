
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.getSubjects),
    path('subjects/<int:subject_id>/questions/', views.getQuestionsBySubjectId),
    path('subjects/<int:subject_id>/questions/<int:question_id>/', views.getQuestionById)
]