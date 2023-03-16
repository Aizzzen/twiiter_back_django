from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

from users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), blank=False)
    fullname = models.CharField(_('fullname'), max_length=255, blank=True)
    username = models.CharField(_('username'), max_length=255, unique=True, blank=False)

    location = models.CharField(_('location'), max_length=255, blank=True)
    about = models.CharField(_('about'), max_length=255, blank=True)
    website = models.CharField(_('website'), max_length=255, blank=True)

    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(_('staff'), default=False)

    is_verified = models.BooleanField(_('verified'), default=False)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        unique_together = ('username', 'email', 'fullname')
