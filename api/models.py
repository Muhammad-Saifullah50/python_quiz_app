from django.db import models

# Create your models here.

class Subject(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
class Question(models.Model):
    subject = models.ForeignKey(Subject, related_name='questions', on_delete=models.CASCADE)
    
    question = models.TextField()
    correct_answer = models.TextField()
    
    def __str__(self):
        return self.question
    
class Answer(models.Model):
    question = models.ForeignKey(Question, related_name="answers", on_delete=models.CASCADE)
    text = models.TextField()
    is_correct = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.text
    
class QuizAttempt(models.Model):
    userId = models.IntegerField()
    score = models.IntegerField()
    subjectId = models.IntegerField()
    
    def __int__(self):
        return self.score