# Generated by Django 4.2.4 on 2023-08-27 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0013_cyclingactivity_date_of_activity_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='activitydata',
            name='pace_chart_image',
            field=models.ImageField(blank=True, null=True, upload_to='pace_charts/'),
        ),
    ]