from django.urls import path

from . import views

app_name = 'data_science'
urlpatterns = [
    path('week1', views.week1, name='week1'),
    path('week1/analysis/', views.twitter_analysis, name='twitter_analysis'),
]