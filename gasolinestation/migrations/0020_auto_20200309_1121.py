# Generated by Django 3.0.3 on 2020-03-09 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0019_gasolinestation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pricemanagement',
            name='gas_station_assigned',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gasolinestation.GasolineStation'),
        ),
    ]
