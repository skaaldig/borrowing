# Generated by Django 2.0.13 on 2019-05-02 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_auto_20190502_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='loan_status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance'), ('o', 'On Loan'), ('a', 'Available')], default='a', max_length=1),
        ),
    ]
