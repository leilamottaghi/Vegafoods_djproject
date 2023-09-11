# Generated by Django 4.2.4 on 2023-09-05 08:04

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
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='نام')),
                ('national_id', models.CharField(max_length=10, unique=True, verbose_name='کد ملی')),
                ('phone_number', models.CharField(max_length=15, verbose_name='شماره تلفن')),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], max_length=10)),
                ('birth_date', models.DateField(blank=True, null=True, verbose_name='تاریخ تولد')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'پروفایل کاربر',
                'verbose_name_plural': 'پروفایل\u200cهای کاربری',
            },
        ),
        migrations.CreateModel(
            name='UserAddressModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=255, verbose_name='آدرس ')),
                ('city', models.CharField(max_length=100, verbose_name='شهر')),
                ('state', models.CharField(max_length=100, verbose_name='استان')),
                ('postal_code', models.CharField(max_length=20, verbose_name='کد پستی')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ایجاد')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر')),
            ],
            options={
                'verbose_name': 'آدرس کاربر',
                'verbose_name_plural': 'آدرس\u200cهای کاربران',
            },
        ),
    ]
