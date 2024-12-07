from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from instrumentarium.accounts.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
    )
    first_name = models.CharField(
        max_length=100,
    )
    last_name = models.CharField(
        max_length=100,
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def delete(self, using=None, keep_parents=False):
        if self.is_staff or self.is_superuser:
            raise ValueError('Cannot deactivate superuser or staff account')

        related_ads = self.ads.all()
        related_ads.update(is_active=False)

        self.is_active = False
        self.save(using=using)

    def __str__(self):
        return self.email

    class Meta:
        permissions = [
            ('can_deactivate_accounts', 'Can activate/deactivate accounts')
        ]


class Profile(models.Model):
    user = models.OneToOneField(
        to=User,
        on_delete=models.CASCADE,
    )
    phone_number = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    profile_image = models.ImageField(
        default='profile/default/default-avatar.jpg',
        upload_to='profile/',
        blank=True,
    )
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.user.email} profile'
