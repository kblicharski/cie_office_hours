# Generated by Django 2.1 on 2018-08-21 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office_hours', '0002_auto_20180821_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='officehoursession',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]