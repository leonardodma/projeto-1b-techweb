from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=1000)
    tag = models.CharField(max_length=200, default="")

    def __str__(self):
        return f'{self.id}. {self.title}'