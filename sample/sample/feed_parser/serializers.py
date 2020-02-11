from feed_parser.models import Repo, Comment, ProgLanguage
from rest_framework import serializers


class RepoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Repo
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class ProgLanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProgLanguage
        fields = '__all__'
