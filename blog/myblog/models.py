from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=32,default='标题')
    content = models.TextField()
