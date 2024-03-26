# Generated by Django 3.2.4 on 2024-03-26 14:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(error_messages={'unique': 'A company with that name already exists'}, max_length=150, unique=True, verbose_name='name company')),
                ('phone', models.CharField(max_length=8, validators=[django.core.validators.RegexValidator(message='Phone number must be entered in the format: +99999999', regex='^\\d{8}$')])),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=150)),
                ('picture', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
