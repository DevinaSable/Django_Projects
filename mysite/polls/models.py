import datetime
from django.utils import timezone

from django.db import models


class Question(models.Model):

    question_text = models.TextField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(selfself):
        return pub_date >= timezone.now()- datetime.timedelta(days=1)


class Choice(models.Model):

    choice_text = models.CharField(max_length=2000)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text

