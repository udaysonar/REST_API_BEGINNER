from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
# Create your models here.

class UserProfileManager(BaseUserManager):
    """Manager For User Profiles"""
    def create_user(self,email,name,password=None):
        """ Create a new User Profile"""
        if not email:
            raise ValueError('Please specify the email address')
        email=self.normalize_email(email)
        user=self.model(email=email,name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self,email,name,password):
        """ Create a new Super User with given details"""
        user=self.create_user(email,name,password)
        user.is_superuser=True
        user.is_staff=True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    """Database Model for users in the system"""
    email=models.EmailField(max_length=256,unique=True)
    name=models.CharField(max_length=255)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    
    objects = UserProfileManager()

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['name']

    def get_full_name(self):
        """Retrive full name of User"""
        return self.name

    def get_short_name(self):
        """Retrive Short name of User"""
        return self.name

    def __str__(self):
        """Return String Representation of User"""
        return self.email

