# Generated by Django 3.0.3 on 2020-03-11 06:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0023_auto_20200311_0612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gasstations',
            name='name',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='gasolinestation.GasolineStation'),
        ),
    ]
