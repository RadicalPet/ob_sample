from feed_parser.models import Repo
from rest_framework import serializers


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'
