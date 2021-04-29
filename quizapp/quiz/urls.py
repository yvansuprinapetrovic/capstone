from django.urls import path
from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("questions/<int:num>", views.questions, name="questions"),
    path("summary", views.summary, name="summary"),

    # API Route
    path("score", views.score, name="score")
]

