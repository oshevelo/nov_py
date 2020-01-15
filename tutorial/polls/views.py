from django.http import HttpResponse
from .models import Choice, Question

from rest_framework import generics
from .serializers import ChoiceSerializer, QuestionSerializer
from django.shortcuts import get_object_or_404


def index(request):
    question_list = Question.objects.all()
    return HttpResponse(', '.join([q.question_text for q in question_list]))


class QuestionList(generics.ListCreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class QuestionDetail(generics.RetrieveDestroyAPIView):
    serializer_class = QuestionSerializer

    def get_object(self):
        return get_object_or_404(Question, pk=self.kwargs.get('question_id'))


class ChoiceList(generics.ListCreateAPIView):
    queryset = Choice.objects.all()
    serializer_class = ChoiceSerializer


class ChoiceDetail(generics.RetrieveDestroyAPIView):
    serializer_class = ChoiceSerializer

    def get_object(self):
        return get_object_or_404(Choice, pk=self.kwargs.get('choice_id'))
