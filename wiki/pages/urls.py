from django.urls import path

from . import views

app_name = "pages"
urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>/edit", views.editPage, name="editPage"),
    path("random", views.randomChoice, name="randomChoice")
]
