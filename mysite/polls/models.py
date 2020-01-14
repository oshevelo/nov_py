import datetime

from django.db import models
from django.utils import timezone


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_description = models.CharField(max_length=200, null=True, blank=True)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{}-{}'.format(self.pk, self.question_text)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return '{}-{}'.format(self.pk, self.choice_text)
