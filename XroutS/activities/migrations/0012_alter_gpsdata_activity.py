# Generated by Django 4.2.4 on 2023-08-24 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0011_activitydata_user_gpsdata_activity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gpsdata',
            name='activity',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='activities.activitydata'),
        ),
    ]
