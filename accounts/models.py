from django.db import models

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin, UserManager
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class UserManager(UserManager):
    use_in_migrations = True
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class CustomUser(AbstractBaseUser,PermissionsMixin):
    """
    An abstract base class implementing a fully featured User model with
    admin-compliant permissions.

    Username and password are required. Other fields are optional.
    """
    # username_validator = UnicodeUsernameValidator()

    # username = models.CharField(
    #     _('username'),
    #     max_length=150,
    #     unique=True,
    #     help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
    #     validators=[username_validator],
    #     error_messages={
    #         'unique': _("A user with that username already exists."),
    #     },
    # )
    # first_name = models.CharField(_('first name'), max_length=30, blank=True)
    # last_name = models.CharField(_('last name'), max_length=150, blank=True)
    email = models.EmailField('email address', unique=True)
    nickname = models.CharField('ニックネーム', max_length=10, blank=False, null=False,default="初期ユーザー")
    created_at = models.DateTimeField('created_at', auto_now=True ,auto_now_add=False)
    is_staff = models.BooleanField(
        'staff status',
        default=False,
        help_text='Designates whether the user can log into this admin site.',
    )
    is_active = models.BooleanField(
        'active',
        default=True,
        help_text=
            'Designates whether this user should be treated as active. '
            'Unselect this instead of deleting accounts.'
        ,
    )
    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'email'
    class Meta:
        verbose_name = 'user'
        verbose_name_plural ='users'
    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)


