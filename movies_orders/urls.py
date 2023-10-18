from django.urls import path
from . import views

urlpatterns = [
    path("movies/<int:movie_id>/orders/", views.MovieOrdersView.as_view()),
]
