# Generated by Django 5.0.2 on 2024-04-01 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locales', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comercio',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='comercios'),
        ),
    ]
