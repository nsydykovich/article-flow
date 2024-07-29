from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.title}"