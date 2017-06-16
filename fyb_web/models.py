from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class LostPet(models.Model):
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    species = models.CharField(
        max_length=255
    )
    breed = models.CharField(
        max_length=255
    )
    description = models.TextField()
    last_seen_location = models.CharField(
        max_length=255
    )
    reward = models.DecimalField(
        blank=True,
        null=True,
        max_digits=6,
        decimal_places=10,
    )


class FoundPet(models.Model):
    finder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=255)
    species = models.CharField(
        max_length=255,
    )
    breed = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
    description = models.TextField()
    last_seen_location = models.CharField(
        max_length=255,
    )