from django.core.validators import MinLengthValidator
from django.db import models

from instrumentarium.ads.choices import InstrumentCondition


class Ad(models.Model):
    title = models.CharField(
        max_length=150,
        validators=[
            MinLengthValidator(10, "Title must contain at least 10 letters")
        ],
    )
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
    )
    image = models.ImageField(
        upload_to='instruments/'
    )
    condition = models.CharField(
        choices=InstrumentCondition.choices,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
