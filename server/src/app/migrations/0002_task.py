# Generated by Django 5.0.7 on 2024-07-18 21:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.TextField(max_length=1000, verbose_name='Description')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Created At')),
                ('updated_at', models.DateField(auto_now=True, verbose_name='Updated At')),
                ('is_complete', models.BooleanField(default=False, verbose_name='Is Complete')),
                ('is_important', models.BooleanField(default=False, verbose_name='Is Important')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Task',
                'verbose_name_plural': 'Tasks',
            },
        ),
    ]
