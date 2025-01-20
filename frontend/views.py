from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests


@login_required
def home(request):
    sub_request = requests.get("http://127.0.0.1:8000/api/subjects")
    subjects = sub_request.json()
    return render(
        request, "home.html", {"username": request.user, "subjects": subjects}
    )


@login_required
def start_quiz(request, subject_id):
    questions_request = requests.get(
        f"http://127.0.0.1:8000/api/subjects/{subject_id}/questions"
    )

    questions = questions_request.json()

    firstQuestionId = questions["data"][0].get("id")

    return render(
        request,
        "start.html",
        {"subjectId": subject_id, "firstQuestionId": firstQuestionId},
    )


@login_required
def quiz(request, subject_id, question_id):
    question_data_response = requests.get(
        f"http://127.0.0.1:8000/api/subjects/{subject_id}/questions/{question_id}/"
    )
    
    data = question_data_response.json()

    question_list_response = requests.get(
        f"http://127.0.0.1:8000/api/subjects/{subject_id}/questions/"
    )

    question_list_data = question_list_response.json()

    question_list = [
        question.get("id") for question in question_list_data.get("data", [])
    ]

    if question_id not in question_list:
        return render(request, "quiz.html", {"error": "Invalid question id"})

    currQuestionIndex = question_list.index(question_id)

    firstQuestion = question_list[0] == question_list[currQuestionIndex]

    attempt_id = request.session.get("attempt_id", None)
    score_request = requests.get(f'http://127.0.0.1:8000/api/quiz-attempt/subjects/{subject_id}/users/{request.user.id}/attempts/{attempt_id}/score')
    
    score = score_request.json()['score']

    if firstQuestion:
        attempt_create_request = requests.post(
            f"http://127.0.0.1:8000/api/quiz-attempt/{subject_id}/{request.user.id}"
        )
        attempt = attempt_create_request.json()
        attempt_id = attempt["data"]["id"]

        request.session['attempt_id'] = attempt_id

    if currQuestionIndex + 1 < len(question_list):
        nextQuestionId = question_list[currQuestionIndex + 1]
    else:
        nextQuestionId = None

    if currQuestionIndex > 0:
        prevQuestionId = question_list[currQuestionIndex - 1]
    else:
        prevQuestionId = None

    if (
        request.method == "POST"
        and request.headers.get("X-Requested-With") == "XMLHttpRequest"
    ):
        correct_answer = data["data"]["question"]["correct_answer"]
        selected_answer = request.POST.get("answer")

        is_correct = selected_answer == correct_answer
        
        if is_correct:
           attempt_score_update_request = requests.post(f'http://127.0.0.1:8000/api/quiz-attempt/subjects/{subject_id}/users/{request.user.id}/attempts/{attempt_id}')
           

        return JsonResponse({"is_correct": is_correct})

    context = {
        "data": data,
        "nextQuestionId": nextQuestionId,
        "prevQuestionId": prevQuestionId,
        "subject_id": subject_id,
        'score': score
        
    }
    return render(request, "quiz.html", context)



