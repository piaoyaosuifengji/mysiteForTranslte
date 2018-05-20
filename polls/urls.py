#! python3
# -- coding: utf-8
from django.urls import path
from . import views


app_name = 'polls'

# urlpatterns = [
#     # ex: /polls/， 通过 name 参数为 URL 定义了名字，你可以在模板中通过 {% url %} 使用它
#     #  查看：polls/templates/polls/index.html
#     path('', views.index, name='index'),
#     path('latest.html', views.index, name='index'),
#     # ex: /polls/5/
#     path('<int:question_id>/', views.detail, name='detail'),
#     # ex: /polls/5/results/
#     path('<int:question_id>/results/', views.results, name='results'),
#     # ex: /polls/5/vote/
#     path('<int:question_id>/vote/', views.vote, name='vote'),
# ]

 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]





