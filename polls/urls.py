#!usr/bin/env python
#---*---coding:utf-8---*---#
__author__ = 'Bruce.张'

from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    path('', views.index, name='index' ),
    
    path('<int:question>/', views.detail, name='detail'),
    path('<int:question/results/', views.results, name='results'),
    path('<int:question_id/vote/', views.vote, name='vote'),

]