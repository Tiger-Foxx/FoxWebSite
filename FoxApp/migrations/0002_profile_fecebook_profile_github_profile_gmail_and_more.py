# Generated by Django 5.0.7 on 2024-09-17 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FoxApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='fecebook',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='github',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='gmail',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedIn',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='youtube',
            field=models.URLField(blank=True),
        ),
    ]
