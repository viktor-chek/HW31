# Generated by Django 4.1.3 on 2022-11-22 07:04

import ads.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0004_alter_user_birth_date_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(null=True, validators=[ads.validators.birth_date]),
        ),
    ]
