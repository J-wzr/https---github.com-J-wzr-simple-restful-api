from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('api/movies/', views.MovieList.as_view(), name='movie-list'),
    path('api/movies/create/', views.create_movie, name='create-movie'),
    path('api/movies/update/<int:pk>/', views.update_movie, name='update-movie'),
    path('api/movies/delete/<int:pk>/', views.delete_movie, name='delete-movie'),
]