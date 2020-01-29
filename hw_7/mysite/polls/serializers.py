from django.contrib.auth.models import User
from rest_framework import serializers
from polls.models import Question
from polls.models import Choice


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ['id',  'question_text', 'question_desc', 'pub_date']

class ChoiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Choice
        fields = ['id','choice_text', 'votes']        
