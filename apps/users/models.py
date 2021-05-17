from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils.translation import ugettext_lazy as _

from apps.users.managers import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    """
    User model class
    """
    first_name = models.CharField(_('first_name'), max_length=50, blank=True, null=True)
    last_name = models.CharField(_('last_name'), max_length=50, blank=True, null=True)
    username = models.CharField(_('username'), max_length=120, unique=True)
    email = models.EmailField(_('email'), unique=True)
    is_staff = models.BooleanField(_('staff_status'), default=False)
    is_active = models.BooleanField(_('active'), default=True)
    date_joined = models.DateTimeField(_('date_joined'), auto_now_add=True)
    is_deleted = models.BooleanField(_('is_deleted'), default=False)

    USERNAME_FIELD = 'email'
    objects = UserManager()

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('-date_joined',)

    def __str__(self):
        return str(self.email)

    def soft_delete(self):
        self.is_deleted = True
        self.save()


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    address = models.CharField(max_length=99, null=True)

