from django.db import models

class Comment(models.Model):
    """Minimal Comment model, implementing only fields needed for sample application""" 
    author = models.CharField(max_length=511)
    body = models.IntegerField()
    created_at = models.DateTimeField()


class ProgLanguage(models.Model):
    name = models.CharField(max_length=511)


class Repo(models.Model):
    """Minimal Repo model, implementing only fields needed for sample application""" 
    name = models.CharField(max_length=511)
    url = models.URLField()
    languages = models.ManyToManyField(ProgLanguage)
