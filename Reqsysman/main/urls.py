from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('Reqsysman', views.Reqsysman),
    path('github', views.github)
]