from django.contrib import admin
from .models import QuizAttempt, Subject, Question, Answer

# Register your models here.

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(QuizAttempt)