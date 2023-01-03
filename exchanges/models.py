from django.conf import settings
from django.db import models

from core.models import BaseModel
from exchanges.enums import ExchangeType


class ExchangeAccount(BaseModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=5, choices=ExchangeType.choices)
    api_key = models.CharField(max_length=255)
    secret_key = models.CharField(max_length=255)
