# type: ignore

from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Subject
from  .serializers import SubjectSerializer


@api_view(['GET'])

def getSubjects(request):
    
    subjects = Subject.objects.all()
    
    serializedSubjects = SubjectSerializer(subjects, many=True)
    
    return Response(serializedSubjects.data)
