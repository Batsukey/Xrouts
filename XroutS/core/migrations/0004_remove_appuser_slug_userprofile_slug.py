# Generated by Django 4.2.4 on 2023-08-09 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_user_id_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appuser',
            name='slug',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='slug',
            field=models.SlugField(default=1, editable=False, unique=True),
            preserve_default=False,
        ),
    ]
