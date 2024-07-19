from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from ..managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField('Email', max_length=40, unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True)
    last_name = models.CharField('Last Name', max_length=255, blank=True)
    is_active = models.BooleanField('Is Active', default=True)
    is_staff = models.BooleanField('Is Staff', default=False)
    is_superuser = models.BooleanField('Is Superuser', default=False)
    birth_date = models.DateField('Birth Date', blank=True, null=True)
    date_joined = models.DateTimeField('Date Joined', auto_now_add=True)    
    
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return f'{str(self.id)} - {str(self.first_name)} {str(self.last_name)}'
    
    def get_email(self):
        return self.email
    
    def get_first_name(self):
        return self.first_name
    
    def get_last_name(self):
        return self.last_name
    
    def get_is_active(self):
        return self.is_active
    
    def get_is_staff(self):
        return self.is_staff
    
    def get_is_superuser(self):
        return self.is_superuser
    
    def get_birth_date(self):
        return self.birth_date
    
    def get_date_joined(self):
        return self.date_joined