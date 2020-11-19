from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('laod-courses', views.load_course, name='ajax_load_courses'),
]