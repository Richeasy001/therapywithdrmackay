# Generated by Django 5.1.5 on 2025-05-06 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0003_sessionbooking_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessionbooking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
