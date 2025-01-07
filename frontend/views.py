from django.shortcuts import render
import requests

def home(request):
    return render(request, 'layout.html')


def quiz(request, subject_id,question_id): 
    
    response = requests.get(f'http://127.0.0.1:8000/api/subjects/{subject_id}/questions/{question_id}/')
    
    data = response.json()
    
    return render(request, 'quiz.html',data)