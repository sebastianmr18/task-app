from django.db import models
from .user_model import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    
    title = models.CharField('Title', max_length=100)
    
    description = models.TextField('Description', max_length=1000)
    
    created_at = models.DateField('Created At', auto_now_add=True)
    
    updated_at = models.DateField('Updated At', auto_now=True)
    
    is_complete = models.BooleanField('Is Complete', default=False)
    
    is_important = models.BooleanField('Is Important', default=False)
    
    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'
        
    def __str__(self):
        return f'{str(self.title)} by {str(self.user.first_name) + " " + str(self.user.last_name)}'