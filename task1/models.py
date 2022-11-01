from django.db import models


# Create your models here.


class TaskOne(models.Model):
    slackUsername = models.CharField(max_length=200)
    backend = models.BooleanField(default=True)
    age = models.IntegerField()
    bio = models.TextField()

    def __str__(self):
        return self.slackUsername
