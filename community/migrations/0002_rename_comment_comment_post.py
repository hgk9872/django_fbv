# Generated by Django 4.1.4 on 2022-12-21 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comment',
            new_name='post',
        ),
    ]
