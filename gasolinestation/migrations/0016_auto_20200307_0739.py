# Generated by Django 3.0.3 on 2020-03-07 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0015_auto_20200304_0942'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pricemanagement',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='transactionsales',
            options={'ordering': ['-created_at']},
        ),
        migrations.AlterModelOptions(
            name='typeoffuel',
            options={'ordering': ['-created_at']},
        ),
        migrations.RemoveField(
            model_name='gasstations',
            name='pricing_for_specific_type_of_fuel',
        ),
        migrations.AddField(
            model_name='gasstations',
            name='fuels',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gasolinestation.TypeOfFuel'),
        ),
    ]
