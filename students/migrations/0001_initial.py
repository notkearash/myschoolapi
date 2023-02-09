# Generated by Django 4.1.4 on 2023-01-22 14:58

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('age', models.IntegerField(validators=[django.core.validators.MaxValueValidator(99)])),
                ('student_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(999999999)])),
            ],
        ),
    ]