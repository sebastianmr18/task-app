from django.db import models
from .user_model import User

class Admin(models.Model):
    USER_ROLES = [
        ('ADMIN', 'Admin'),
        ('EMPLOYEE', 'Employee'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    
    role = models.CharField('Rol', max_length=30, choices=USER_ROLES, blank=True, null=True)
    
    class Meta:
        verbose_name = 'Admin'
        verbose_name_plural = 'Admins'
        
    def __str__(self):
        return f'{str(self.user)}'
    
    def get_user(self):
        return self.user
    
    def get_role(self):
        return self.role
    
    def user_id(self):
        return self.user.id
    