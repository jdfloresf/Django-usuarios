# Generated by Django 5.1 on 2024-08-23 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombres',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
