# Generated by Django 2.1 on 2018-08-21 06:15

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        ('office_hours', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='OfficeHours',
            new_name='OfficeHour',
        ),
        migrations.RenameModel(
            old_name='OfficeHoursSession',
            new_name='OfficeHourSession',
        ),
        migrations.RenameField(
            model_name='officehoursession',
            old_name='office_hours',
            new_name='office_hour',
        ),
        migrations.RenameField(
            model_name='studentqueue',
            old_name='office_hours_session',
            new_name='office_hour_session',
        ),
    ]