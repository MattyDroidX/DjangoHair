# Generated by Django 4.2.8 on 2024-01-04 22:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='openinghours',
            name='week_number',
        ),
    ]
