from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('question/', views.QuestionList.as_view(), name='questions_list'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='question_detail'),

    path('choice/', views.ChoiceList.as_view(), name='choices_list'),
    path('choice/<int:choice_id>', views.ChoiceDetail.as_view(), name='choice_detail')
]
