from django.contrib.auth.models import User
from django.db import models


class LostPet(models.Model):
    """
    Purpose: Creates Lost Pet table within the database
    Author: Max Baldridge
    Arguments: models.Models: (NA): models calss given by django
    Returns: (None): N/A
    """
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=255
    )
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
    contact_info = models.TextField()