# Generated by Django 2.0.13 on 2019-04-03 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_auto_20190403_0949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productinstance',
            name='returned',
            field=models.DateField(blank=True, null=True),
        ),
    ]