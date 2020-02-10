from django.urls import path
from .views import *
from .registration_view import registration_view
from rest_framework.authtoken import views

app_name = 'movies'

urlpatterns = [

    path('genres/create', GenreCreateAPIView.as_view(), name='genre-create'),
    path('genre/<int:id>/update/', GenreUpdateAPIView.as_view(), name='genre-update'),
    path('film/', FilmCreateAPIView.as_view(), name='film-create'),

    path('user/register/', registration_view, name='register'),
    path('user/login/', views.obtain_auth_token,name='login')

]
