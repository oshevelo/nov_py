from django.http import HttpResponse
from django.http import Http404
from rest_framework import generics
from django.shortcuts import render, get_object_or_404

from polls.models import Question
#from polls.serializers import QuestionSerializer


def index(request):
    question_list = Question.objects.all()
    return HttpResponse(', '.join([q.question_text for q in question_list]))


def index_other(request):
    return HttpResponse("Hello, OTHER world. You're at the polls index.")

'''
class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = QuestionSerializer

    def get_object(self):
        obj = get_object_or_404(Question, pk=self.kwargs.get('question_id'))
        return obj

'''
