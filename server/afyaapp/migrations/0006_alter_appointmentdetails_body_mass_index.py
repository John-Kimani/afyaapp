# Generated by Django 4.2 on 2023-06-12 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afyaapp', '0005_alter_appointmentdetails_appointment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointmentdetails',
            name='body_mass_index',
            field=models.DecimalField(decimal_places=1, max_digits=5),
        ),
    ]
