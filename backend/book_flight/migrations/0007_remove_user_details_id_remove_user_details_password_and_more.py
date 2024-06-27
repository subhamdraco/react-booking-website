# Generated by Django 5.0.6 on 2024-06-27 09:00

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_flight', '0006_remove_seat_passenger_type'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_details',
            name='id',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='password',
        ),
        migrations.RemoveField(
            model_name='user_details',
            name='user_name',
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_add',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_city',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_country',
            field=models.CharField(default=' ', max_length=40),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_name',
            field=models.TextField(default=' '),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_pincode',
            field=models.CharField(default=' ', max_length=20),
        ),
        migrations.AddField(
            model_name='user_details',
            name='ag_state',
            field=models.CharField(default=' ', max_length=40),
        ),
        migrations.AddField(
            model_name='user_details',
            name='mobile',
            field=models.CharField(default=1, max_length=20, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='bookingdetails',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]