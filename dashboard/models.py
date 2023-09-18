from django.db import models


class Analysis(models.Model):
    title = models.CharField(max_length=150)
    picture = models.URLField()
    description = models.TextField()

    def __str__(self):
        return self.title
