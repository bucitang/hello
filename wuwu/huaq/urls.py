import django.urls import path

import . import views

urlpatterns = [
    path("", views.index, name="index")
]