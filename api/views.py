# type: ignore

from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def test(request):
    person = {'name': 'Saif', 'age': '19'}
    return Response(person)
