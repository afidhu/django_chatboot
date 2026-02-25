from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# from .utils import get_answer
# import json

# chat_ui/views.py
from .chatbot import ask_question

@csrf_exempt
def chat_view(request):
    answer = None
    if request.method == "POST":
        question = request.POST.get("question")
        answer = ask_question(question)
        print(f"Question: {question}, Answer: {answer}")
    return JsonResponse({"answer": answer})
    # return render(request, "chat_ui/index.html", {"answer": answer})