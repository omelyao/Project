from django.urls import re_path

from . import views

urlpatterns = [
    re_path('^$', views.index, name='index'),
    re_path('importance/', views.importance, name='importance'),
    re_path('geography/', views.geography, name='geography'),
    re_path('skills/', views.skills, name='skills'),
    re_path('vacancies/', views.last_vacancies, name='vacancies'),
]
