from django.shortcuts import render
from django.http import Http404, HttpResponse
from .models import Question, Answers, Score
from django.http import JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
import random
from .models import Question, Answers, Score, Backgrounds

# Create your views here.

scoreId = []

def index(request):

    number = random.randint(1, 10000)
    scoreId.append(number)
    
    # creating score for session
    score = Score(points=0, number=number)
    score.save()
    
    return render(request, "quiz/index.html")

def questions(request, num):
    if 1 <= num <= 10:
        question = Question.objects.get(pk=num)
        answers = Answers.objects.filter(question=question)
        image = Backgrounds.objects.get(pk=num)
        questionNumber = num

        return render(request, "quiz/questions.html", {
        "question": question,
        "answers": answers,
        "questionNumber": questionNumber,
        "image": image
    })
    else:
        raise Http404("No such section")
    

@csrf_exempt
def score(request):
    number = scoreId[-1]
    # Query for requested score
    try:
        currentScore = Score.objects.get(number=number)
    except:
        return JsonResponse({"error": "Score not found."}, status=404)


    #Update score
    if request.method == "PUT":
        # Get data
        data = json.loads(request.body)
        # Get new score
        addScore = data.get("points", "")
        # Calculate new score
        points = currentScore.points + addScore
        #Update score
        currentScore.points = points
        #Save
        currentScore.save()
        return JsonResponse({"message": "Score updatef successfully."}, status=201)
    
    # POST must be via PUT
    else:
        return JsonResponse({
            "error": "PUT request required."
        }, status=400)

def summary(request):
    # Query for requested score
    number = scoreId[-1]
    try:
        currentScore = Score.objects.get(number=number)
    except:
        return JsonResponse({"error": "Score not found."}, status=404)

    final = currentScore.points

    return render(request, "quiz/summary.html", {
        "final": final
    })