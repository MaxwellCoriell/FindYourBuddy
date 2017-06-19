from django.contrib.auth.models import User
from django.db import models


class FoundPet(models.Model):
    """
    Purpose: Creates Found Pet table within the database
    Author: Max Baldridge
    Arguments: models.Models: (NA): models calss given by django
    Returns: (None): N/A
    """
    finder = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        blank=True,
        null=True,
        max_length=255,
    )
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
        max_length=255
    )
    contact_info = models.TextField()