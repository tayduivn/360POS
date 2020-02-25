# Generated by Django 3.0.3 on 2020-02-25 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='FuelPricing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('currency', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GasStations',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=150, null=True)),
                ('site_location', models.CharField(blank=True, max_length=150, null=True)),
                ('price_management_flexibility', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('pricing_for_specific_type_of_fuel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gasolinestation.FuelPricing')),
                ('site_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='site_managers', to=settings.AUTH_USER_MODEL)),
                ('site_staff', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='site_staffs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]