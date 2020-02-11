from django.urls import include, path
from rest_framework import routers

from feed_parser import views

urlpatterns = [
    path("/", include("rest_framework.urls", namespace="rest_framework")),
    path("repos", views.RepoViewSet.as_view()),
    path("comments", views.CommentViewSet.as_view()),
    path("languages", views.ProgLanguageViewSet.as_view()),
]
