from rest_framework import generics, viewsets

from feed_parser.models import *
from feed_parser.serializers import (CommentSerializer, ProgLanguageSerializer,
                                     RepoSerializer)


class RepoViewSet(generics.ListAPIView):
    """
    API endpoint 
    """

    serializer_class = RepoSerializer

    def get_queryset(self):
        limit = self.request.query_params.get("limit", None)
        queryset = Repo.objects.all().order_by("-created_at")
        if limit is not None:
            queryset = queryset[: int(limit)]
        return queryset


class CommentViewSet(generics.ListAPIView):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class ProgLanguageViewSet(generics.ListAPIView):
    serializer_class = ProgLanguageSerializer
    queryset = ProgLanguage.objects.all()
