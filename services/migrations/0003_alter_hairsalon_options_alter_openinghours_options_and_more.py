# Generated by Django 4.2.8 on 2024-01-08 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_remove_openinghours_week_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='hairsalon',
            options={'verbose_name_plural': 'Salon'},
        ),
        migrations.AlterModelOptions(
            name='openinghours',
            options={'verbose_name_plural': 'Horarios'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'ordering': ['id'], 'verbose_name_plural': 'Servicios'},
        ),
        migrations.AlterModelOptions(
            name='timeslot',
            options={'verbose_name_plural': 'Turnos'},
        ),
        migrations.AddField(
            model_name='service',
            name='duration',
            field=models.IntegerField(default=40),
            preserve_default=False,
        ),
    ]
