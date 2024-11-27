from django.db import models


class InstrumentCondition(models.TextChoices):
    NEEDS_REPAIR = 'R', 'Needs repair'
    BAD = 'B', 'Bad'
    GOOD = 'G', 'Good'
    VERY_GOOD = 'VG', 'Very good'
    LIKE_NEW = 'LN', 'Like new'
    NEW = 'N', 'New'

