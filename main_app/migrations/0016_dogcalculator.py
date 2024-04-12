# Generated by Django 5.0.3 on 2024-04-11 23:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_rename_cat_photo_dog'),
    ]

    operations = [
        migrations.CreateModel(
            name='DogCalculator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('activity', models.CharField(choices=[('typical', 60.82), ('active', 69.18), ('overweight', 38.77), ('high_activity', 96.92), ('senior', 49.79), ('inactive', 49.79), ('light_duty', 77.36), ('med_duty', 89.99), ('high_duty', 117.63)])),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.dog')),
            ],
        ),
    ]
