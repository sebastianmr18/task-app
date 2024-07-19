from django.contrib import admin
from .models.user_model import User
from .models.admin_model import Admin
from .models.task_model import Task

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff', 'is_active')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('is_staff', 'is_active')
    ordering = ('email',)
    readonly_fields = ('date_joined',)
    list_per_page = 10
    fieldsets = (
        ('Información de Cuenta', {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name')}),
        ('Permisos', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Fechas', {'fields': ('date_joined', 'birth_date')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_active'),
        }),
    )    

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ('user_id','user', 'role')
    list_per_page = 10
    
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'title', 'description', 'created_at', 'updated_at', 'is_complete', 'is_important')
    search_fields = ('id','user', 'title', 'description')
    readonly_fields = ('created_at', 'updated_at')
    list_per_page = 10
    
    
