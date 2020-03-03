# Generated by Django 3.0.3 on 2020-03-03 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gasolinestation', '0007_auto_20200303_1103'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImportantInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('created_by', models.CharField(blank=True, max_length=150, null=True)),
                ('updated_by', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
    ]
