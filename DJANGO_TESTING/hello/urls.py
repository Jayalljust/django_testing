from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name ="index"),
    path("<str:name>", views.greet, name="greet"),
    path("seva", views.seva, name="seva"),
    path("tema", views.tema, name="tema")
]