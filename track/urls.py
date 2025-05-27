from django.urls import path

from tracker.track.migrations import views

urlpatterns = [
    path("", views.index, name="index"),
]