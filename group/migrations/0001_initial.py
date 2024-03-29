# Generated by Django 5.0.1 on 2024-01-27 12:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('major', models.CharField(max_length=300)),
                ('about', models.TextField()),
                ('telegram', models.CharField(max_length=200)),
                ('instagram', models.CharField(max_length=200)),
                ('github', models.CharField(max_length=300)),
                ('gmail', models.EmailField(max_length=254)),
                ('picture', models.ImageField(upload_to='media/')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
