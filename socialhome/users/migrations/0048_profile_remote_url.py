# Generated by Django 3.2.18 on 2023-07-22 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0047_auto_20230401_2229'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='remote_url',
            field=models.URLField(blank=True, editable=False, max_length=255, null=True, unique=True, verbose_name='Profile URL'),
        ),
    ]
