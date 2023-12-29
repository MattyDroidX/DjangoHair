# Generated by Django 4.2.8 on 2023-12-27 19:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=254)),
                ('email', models.EmailField(help_text='Ingrese su dirección de correo electrónico', max_length=254)),
                ('phone', models.CharField(help_text='Ingrese el número de teléfono celular', max_length=15)),
                ('booking_date', models.DateField(auto_now_add=True)),
                ('is_confirmed', models.BooleanField(default=False)),
                ('salon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='salon_booking', to='services.hairsalon')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='service_booking', to='services.service')),
                ('timeslot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='time_slot_booking', to='services.timeslot')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
                'ordering': ['timeslot'],
                'unique_together': {('salon', 'timeslot')},
            },
        ),
    ]
