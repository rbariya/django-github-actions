from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):
        """
        creates and saves a User with the given email and password.
        """
        email = self.normalize_email(email)
        user = self.model(email=email, is_staff=is_staff, is_active=True,
                          is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, is_staff=False, is_superuser=False, **extra_fields):
        return self._create_user(email, password, is_staff, is_superuser, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)
