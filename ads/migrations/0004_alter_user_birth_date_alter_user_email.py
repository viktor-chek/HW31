# Generated by Django 4.1.3 on 2022-11-21 11:29

import ads.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateTimeField(null=True, validators=[ads.validators.birth_date]),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, validators=[django.core.validators.RegexValidator(inverse_match=True, message='Регистрация с домена rumbler.ru запрещена', regex='rumbler.ru')], verbose_name='email address'),
        ),
    ]
