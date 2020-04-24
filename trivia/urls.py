from django.urls import path

from . import views

app_name = 'trivia'
urlpatterns = [
    path('', views.trivia_game, name='trivia_game'),
    path('categories', views.trivia_game_categories, name='trivia_game_categories'),
]