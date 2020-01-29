from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    question_desc = models.CharField(max_length=200, default="")
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return '{} {}'.format(self.id, self.question_text)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=1)

    def __str__(self):
        return '{} {}'.format(self.id, self.choice_text, self.votes)
