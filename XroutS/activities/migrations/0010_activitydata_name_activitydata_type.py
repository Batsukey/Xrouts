# Generated by Django 4.2.4 on 2023-08-24 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0009_activitydata'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydata',
            name='name',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='activitydata',
            name='type',
            field=models.CharField(default=1),
            preserve_default=False,
        ),
    ]
