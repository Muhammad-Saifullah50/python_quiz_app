
from django.urls import path
from . import views

urlpatterns = [
    path('subjects/', views.getSubjects),
    path('subjects/<int:subject_id>/questions/', views.getQuestionsBySubjectId),
    path('subjects/<int:subject_id>/questions/<int:question_id>/', views.getQuestionById, name='quiz_question'),
    path('quiz-attempt/<int:subject_id>/<int:user_id>', views.createQuizAttempt, name='createQuizAttempt')
]