from django.db import models


class Regex(models.Model):
    id = models.AutoField(primary_key=True)
    entry = models.CharField(max_length=512, unique=True)
    description = models.TextField()


class DataLeak(models.Model):
    id = models.AutoField(primary_key=True)
    message = models.TextField()
    catching_regex = models.ForeignKey(Regex, on_delete=models.CASCADE)
