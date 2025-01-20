from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Answer, Question, Subject
from .serializers import AnswerSerializer, QuestionSerializer, SubjectSerializer


@api_view(["GET"])
def getSubjects(request):
    subjects = Subject.objects.all()

    if not subjects:
        return Response({"message": "Subjects not found"}, status=404)

    serializedSubjects = SubjectSerializer(subjects, many=True)

    return Response(
        {"message": "Subjects retrieved successfully", 
         "data": serializedSubjects.data},
        status=200,
    )


@api_view(["GET"])
def getQuestionsBySubjectId(request, subject_id):
    questions = Question.objects.filter(subject_id=subject_id)
    serializedQuestions = QuestionSerializer(questions, many=True)

    return Response(
        {
            "message": "Questions retrieved successfully",
            "data": serializedQuestions.data,
        },
        status=200,
    )


@api_view(["GET"])
def getQuestionById(request, subject_id, question_id):
    question = Question.objects.filter(subject_id=subject_id, id=question_id).first()

    if not question:
        return Response({"message": "question not found"}, status=404)

    serializedQuestion = QuestionSerializer(question)

    answers = Answer.objects.filter(question_id=question_id)
    serializedAnswers = AnswerSerializer(answers, many=True)

    data = {"question": serializedQuestion.data, "answers": serializedAnswers.data}

    return Response(
        {"message": "Question retrieved successfully", "data": data}, status=200
    )

@api_view (['POST'])
def quizAttempt(request, subject_id):
    pass