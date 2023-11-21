from datetime import datetime
from django.db import models


class Author(models.Model):
    username = models.CharField(max_length=20)



# Create your models here.
class Exercice(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    created_at = models.DateTimeField(editable=False, default=datetime.now())
    resultat = models.IntegerField(default=0, null=False)

    