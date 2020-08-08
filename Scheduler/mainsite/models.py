from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, account, password, email):
        if not account:
            raise ValueError("Users must have an account")
        if not password:
            raise ValueError("Users must have a password")
        
        user = self.model(
            account = account,
            email = self.normalize_email(email),
        )
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, account, password, email):
        user = self.create_user(
                account = account,
                password = password,
                email = email,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    account = models.CharField(max_length=10, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=255, unique=True) 
    date = models.DateTimeField(default=timezone.now)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'account'
    REQUIRED_FIELDS = ['password', 'email']

    objects = UserManager()

    def __str__(self):
        return self.account
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


