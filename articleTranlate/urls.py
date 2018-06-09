#! python3
# -- coding: utf-8
from django.urls import path
from . import views


app_name = 'articleTranlate'

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
    path('', views.articleView.as_view(), name='index'),
    # path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    # path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('articleTranlate/updataArticle/', views.updataArticle, name='updataArticle'),
    path('articleTranlate/ajax_list/', views.ajax_list, name='ajax_list'),
    path('articleTranlate/ajax_dict/', views.ajax_dict, name='ajax_dict'),
    path('articleTranlate/ArticleAddress/', views.getArticleAddress, name='getArticleAddress'),
    path('articleTranlate/get_one_word/', views.get_one_word, name='get_one_word'),
    path('articleTranlate/post_save_one_str/', views.post_save_one_str, name='post_save_one_str'),
    path('articleTranlate/save_into_doc/', views.save_into_doc, name='save_into_doc'),
]



    # url(r'^ajax_list/$', 'tools.views.ajax_list', name='ajax-list'),
    # url(r'^ajax_dict/$', 'tools.views.ajax_dict', name='ajax-dict'),

