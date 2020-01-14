import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=50)
    question_desc = models.CharField(max_length=255, default='')
    pub_date = models.DateTimeField('date published', auto_now_add=True, blank=True)

    def was_published_recently(self):\
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return '{} {}'.format(self.id, self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=255)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '{} {}'.format(self.id, self.question)
