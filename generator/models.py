from django.db import models
from django.conf import settings


class Password(models.Model):
    service = models.CharField(max_length=50, blank=False, verbose_name="Ресурс")
    password_for_the_service = models.CharField(max_length=20, blank=False, verbose_name="Пароль")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service
