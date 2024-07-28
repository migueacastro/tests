from django.urls import path
from films.views import *

urlpatterns = [
    path('films/', FilmListAPIView.as_view()), # / api / films
    path('films/<int:pk>/', FilmDetailAPIView.as_view())
]