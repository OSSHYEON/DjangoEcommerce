from django.urls import path
from . import views

app_name='board'

urlpatterns =[
    path('notice/', views.notice_list, name='notice'),
    path('notice/<int:pk>/', views.notice_detail, name='notice_detail'),
    path('', views.question_list, name='question_list'),
    path('question_create/', views.question_create, name='question_create'),
    path('<int:pk>/', views.question_detail, name='question_detail'),
    path('info/', views.company_info, name='company_info'),
]