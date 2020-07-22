from django.urls import path

from . import views


app_name = "display"
urlpatterns = [
    path("<str:entry>", views.index, name="index")
]
