# Generated by Django 4.2.1 on 2023-05-16 19:51

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='OTPUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('secret_key', models.CharField(default='TEO7EK2DUAIAMK5XJVZVNWJX3572AXDU', max_length=32)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=6, null=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime(2023, 5, 16, 19, 51, 34, 603957, tzinfo=datetime.timezone.utc), editable=False)),
                ('otp_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='otp.otpuser')),
            ],
        ),
    ]
