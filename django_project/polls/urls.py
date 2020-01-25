from django.urls import path

from . import views

urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/5/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
    # /polls/choices/
    path('choices/', views.ChoiceList.as_view(), name='choices'),
    # /polls/choices/2/
    path('choices/<int:choice_id>/', views.ChoiceDetail.as_view(), name='choice'),
    # /polls/question/
    path('question/', views.QuestionList.as_view(), name='questions'),
    # /polls/question/3/
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='question')
]