from django.urls import path

from . import views

app_name = 'mv'


urlpatterns = [
    path('', views.index, name='index'),
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/question/create/', views.question_create, name='question_create'),
    path('<int:movie_id>/question/<int:question_id>/modify/', views.question_modify, name='question_modify'),
    path('<int:movie_id>/question/<int:question_id>/delete', views.question_delete, name='question_delete'),
]