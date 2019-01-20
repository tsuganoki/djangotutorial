from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('age', views.AgeProfile, name='age-profile')
]