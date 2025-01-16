from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import requests

@login_required
def home(request):
    return render(request, "layout.html")


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

        return JsonResponse({"is_correct": is_correct})

    context = {
        "data": data,
        "nextQuestionId": nextQuestionId,
        "prevQuestionId": prevQuestionId,
        "subject_id": subject_id,
    }
    return render(request, "quiz.html", context)
