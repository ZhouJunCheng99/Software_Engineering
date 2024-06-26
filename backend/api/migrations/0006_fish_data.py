# Generated by Django 2.1.4 on 2024-06-27 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_message_phone_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fish_Data',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('species', models.CharField(max_length=50, null=True)),
                ('body_length', models.FloatField(null=True)),
                ('body_weight', models.FloatField(null=True)),
                ('health_status', models.CharField(max_length=20, null=True)),
                ('fish_group_status', models.CharField(max_length=20, null=True)),
                ('breeding_period', models.CharField(max_length=20, null=True)),
                ('fish_group_total', models.FloatField(null=True)),
                ('fry_number', models.FloatField(null=True)),
                ('adult_fish_number', models.FloatField(null=True)),
            ],
        ),
    ]
