from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser,User
from django.conf import settings
from django.contrib.auth.models import BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, birthdate, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            birthdate=birthdate,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, birthdate, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
            birthdate=birthdate,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user 

class CustomUser(AbstractBaseUser):
    #user=models.OneToOneField(User,on_delete=models.CASCADE)
    username=models.CharField(verbose_name='user name',max_length=10,unique=True)
    email = models.EmailField(verbose_name='email address',max_length=255,unique=True,)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    phonenumber=models.CharField(verbose_name="phone number", max_length=10)
    birthdate=models.DateField(auto_now=False, auto_now_add=False,verbose_name='birth date')
    nickname=models.CharField(verbose_name='nick name', max_length=6)
    is_active=models.BooleanField(default=True)
    is_admin=models.BooleanField(default=False)
    last_login=models.DateTimeField(auto_now=True)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email' 
 
   