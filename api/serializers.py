
from rest_framework import serializers
from api.models import Answer, Question, QuizAttempt, Subject

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
       model = Subject
       fields = '__all__'
       
       
class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'
        
class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = '__all__'
    
class QuizAttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = QuizAttempt
        fields = '__all__'