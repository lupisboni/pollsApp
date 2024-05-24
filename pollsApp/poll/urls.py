from django.urls import path

from . import views

app_name ='poll'
urlpatterns =[
    path('', views.home,name='home'),
    #localhost:8000/poll/1/vote/
    path('<int:q_id>/vote/', views.vote, name='vote'),
    #localhost:8000/poll/1/result/
    path('<int:q_id>/result/',  views.result, name='result')
]