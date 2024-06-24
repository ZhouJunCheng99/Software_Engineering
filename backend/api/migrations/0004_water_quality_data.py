# Generated by Django 2.1.4 on 2024-05-23 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_message_permission'),
    ]

    operations = [
        migrations.CreateModel(
            name='Water_Quality_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('monitoring_time', models.CharField(max_length=30, null=True)),
                ('water_quality_category', models.CharField(max_length=10, null=True)),
                ('water_temperature', models.FloatField(null=True)),
                ('pH', models.FloatField(null=True)),
                ('dissolved_oxygen', models.FloatField(null=True)),
                ('conductivity', models.FloatField(null=True)),
                ('turbidity', models.FloatField(null=True)),
                ('permanganate_index', models.FloatField(null=True)),
                ('ammonia_nitrogen', models.FloatField(null=True)),
                ('total_phosphorus', models.FloatField(null=True)),
                ('total_nitrogen', models.FloatField(null=True)),
                ('site_status', models.CharField(max_length=20, null=True)),
            ],
        ),
    ]
