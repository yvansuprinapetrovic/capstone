from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question, Answers

# Create your views here.

def index(request):
    return render(request, "quiz/index.html")

def questions(request, num):
    if 1 <= num <= 10:
        question = Question.objects.get(pk=num)
        answers = Answers.objects.filter(question=question)
        questionNumber = num
        return render(request, "quiz/questions.html", {
        "question": question,
        "answers": answers,
        "questionNumber": questionNumber
    })
    else:
        raise Http404("No such section")