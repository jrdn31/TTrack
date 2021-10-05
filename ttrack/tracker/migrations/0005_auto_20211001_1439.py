# Generated by Django 3.2.6 on 2021-10-01 22:39

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20210830_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='desired_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='request',
            name='loan_length',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1, message='Loans cannot be shorter than one day.'), django.core.validators.MaxValueValidator(10, message='Loans cannot be longer than 10 days.')]),
            preserve_default=False,
        ),
    ]
