from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('other/', views.index_other, name='index'),
    path('question/', views.QuestionList.as_view(), name='question_list'),
    path('question/<int:question_id>/', views.QuestionDetail.as_view(), name='question_details'),
    path('choice/', views.ChoiceList.as_view(), name='choice_list'),
    path('choice/<int:choice_id>/', views.ChoiceDetail.as_view(), name='choice_details'),

    # ex: /polls/
    #path('', views.index, name='index'),
    # ex: /polls/5/
    #path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
    #path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
