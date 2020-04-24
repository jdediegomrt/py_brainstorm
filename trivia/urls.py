from django.urls import path

from . import views

app_name = 'trivia'
urlpatterns = [
    path('questions', views.trivia_game_questions, name='trivia_game_questions'),
    path('categories', views.trivia_game_categories, name='trivia_game_categories'),
]