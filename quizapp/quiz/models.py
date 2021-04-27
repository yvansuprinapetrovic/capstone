from django.contrib.auth.models import AbstractUser
from django.db import models

class Question(models.Model):

    # Question asked
    prompt = models.CharField(max_length=1500)

    def serialize(self):
        return {
            "prompt": self.prompt
        }
    
    def __str__(self):
        return f"{self.prompt}"

class Answers(models.Model):
    # Related question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # Multiple choice
    text = models.CharField(max_length=1000)
    # Correct answer
    correct = models.BooleanField(default=False)

    def serialize(self):
        return {
            "question": self.question,
            "text": self.text,
            "correct": self.text
        }

    def __str__(self):
        return f"{self.text}"