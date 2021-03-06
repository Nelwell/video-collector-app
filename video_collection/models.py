from django.db import models


class Video(models.Model):
    name = models.CharField(max_length=200)
    url = models.CharField(max_length=400)
    notes = models.TextField(blank=True, null=True)  # blank=True allows field to be blank, null=True allows null values in db

    def __str__(self):
        return f'ID: {self.pk}, Name: {self.name}, URL; {self.url}, Notes: {self.notes[:200]}'
