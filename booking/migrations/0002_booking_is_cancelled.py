# Generated by Django 4.2.8 on 2024-01-02 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='is_cancelled',
            field=models.BooleanField(default=False),
        ),
    ]
