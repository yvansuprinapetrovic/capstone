from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answers

# Create your views here.

def index(request):
    return render(request, "quiz/index.html")

def questions(request):
    question = Question.objects.get(pk=1)
    answers = Answers.objects.filter(question=question)
    questionNumber = 1
    return render(request, "quiz/questions.html", {
        "question": question,
        "answers": answers,
        "questionNumber": questionNumber
    })