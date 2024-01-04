# Generated by Django 4.2.8 on 2024-01-04 19:58

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HairSalon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=datetime.date.today)),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('is_closed', models.BooleanField()),
                ('week_number', models.IntegerField()),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.hairsalon')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('service_type', models.CharField(choices=[('Corte de cabello', 'Corte de cabello'), ('Corte y barba', 'Corte y barba')], max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={
                'verbose_name_plural': 'Services',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='TimeSlot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('is_blocked', models.BooleanField()),
                ('is_reservated', models.BooleanField(default=False)),
                ('duration', models.IntegerField(default=40)),
                ('opening_hours', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.openinghours')),
            ],
        ),
    ]
