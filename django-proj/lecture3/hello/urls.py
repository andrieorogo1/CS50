from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("andrie", views.andrie, name="andrie"),
    path("christian", views.christian, name="christian")
]