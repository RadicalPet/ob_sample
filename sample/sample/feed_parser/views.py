from feed_parser.models import *
from rest_framework import viewsets
from feed_parser.serializers import RepoSerializer

class RepoViewSet(viewsets.ModelViewSet):
    """
    API endpoint 
    """
    queryset = Repo.objects.all()
    serializer_class = RepoSerializer
