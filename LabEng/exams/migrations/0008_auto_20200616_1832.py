# Generated by Django 3.0.4 on 2020-06-16 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0007_auto_20200602_2031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='realization_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
