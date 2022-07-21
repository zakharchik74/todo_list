from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
from django.conf import settings


class ToDo(models.Model):
    to_do = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
class ToDo_process(models.Model):
    to_do = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
class ToDo_completed(models.Model):
    to_do = models.TextField()
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )