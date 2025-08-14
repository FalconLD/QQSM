from django.urls import path
from . import views

urlpatterns = [
    # URLs del menú y gestión
    path('', views.home, name='home'),
    path('manage/', views.manage_questions, name='manage_questions'),
    path('manage/add/', views.add_question, name='add_question'),
    path('manage/edit/<int:pk>/', views.edit_question, name='edit_question'),
    path('manage/delete/<int:pk>/', views.delete_question, name='delete_question'),
    path('shutdown/', views.shutdown_server, name='shutdown'),
    
    # URLs del juego
    path('play/', views.play, name='play'),
    path('play/question/<int:pk>/', views.play_question, name='play_question'),
    path('play/answer/<int:pk>/', views.answer_question, name='answer_question'),
]