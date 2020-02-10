from django.contrib.auth.models import User
from django.db import models

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


# Create your models here.

class Genre(models.Model):
    title = models.CharField(max_length=25, unique=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='genre_created_by')
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='genre_modified_by', blank=True,
                                    null=True)
    modified_date = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return self.title


class Film(models.Model):
    title = models.CharField(max_length=50, unique=True)
    cover_image = models.ImageField()
    released_date = models.DateField()
    genre = models.ManyToManyField(Genre)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='film_created_by')
    created_date = models.DateField(auto_now_add=True)
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='film_modified_by', blank=True,
                                    null=True)
    modified_date = models.DateField(blank=True, auto_now=True)

    def __str__(self):
        return self.title


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
