# from django.contrib.auth.models import User
from rest_framework import serializers
from polls.models import Question, Choice


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('id', 'question_text', 'pub_date', 'was_published_recently')


class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ('id', 'question', 'choice_text', 'votes')
