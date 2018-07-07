from django.db import models
from django.utils import timezone
# Create your models here.


class User(models.Model):
    """docstring for User"""
    name = models.CharField(max_length=32, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField(unique=True)
    time = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"
