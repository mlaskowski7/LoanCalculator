# Generated by Django 4.2.7 on 2023-11-16 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LoanCalculatorAPI', '0003_alter_loan_lending_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loan',
            name='lending_rate',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='loan',
            name='value',
            field=models.IntegerField(default=0),
        ),
    ]