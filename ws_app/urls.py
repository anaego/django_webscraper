from django.urls import path

from ws_app import views

urlpatterns = [
    path("", views.home, name="home"),
]