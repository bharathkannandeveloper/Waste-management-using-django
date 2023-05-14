# Generated by Django 3.0.1 on 2020-03-16 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_remove_myuser_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='account_type',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Select Account'), (1, 'Seller'), (2, 'Buyer')], default=0),
        ),
        migrations.AddField(
            model_name='myuser',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='myuser',
            name='contact',
            field=models.CharField(default='+88', max_length=255),
        ),
    ]