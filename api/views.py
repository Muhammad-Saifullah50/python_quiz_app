# type: ignore

from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Answer, Question, Subject
from  .serializers import AnswerSerializer, QuestionSerializer, SubjectSerializer


@api_view(['GET'])

def getSubjects():
    
    subjects = Subject.objects.all()
    
    serializedSubjects = SubjectSerializer(subjects, many=True)
    
    return Response(serializedSubjects.data)

@api_view(['GET'])

def getQuestionsBySubjectId(request, subject_id):
    
    questions = Question.objects.filter(subject_id = subject_id)
    serializedQuestions = QuestionSerializer(questions, many=True)
    
    return Response(serializedQuestions.data)
    
    
@api_view(['GET'])

def getQuestionById(request, subject_id, question_id):
    
    question = Question.objects.filter(subject_id = subject_id, id = question_id ).first()
    
    if not question: 
        return Response({'message': 'question not found'}, status=404)
    
    serializedQuestion = QuestionSerializer(question)
    
    answers = Answer.objects.filter(question_id = question_id)
    serializedAnswers = AnswerSerializer(answers, many=True)
    
    data = {
        'question': serializedQuestion.data,
        'answers': serializedAnswers.data
    }

    return Response(data)
    
