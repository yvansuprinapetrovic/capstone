from django.contrib import admin

from .models import Question, Answers, Score

# Register your models here.
admin.site.register(Question)
admin.site.register(Answers)
admin.site.register(Score)
