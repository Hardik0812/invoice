# Generated by Django 4.0.4 on 2022-04-14 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currency',
            old_name='id',
            new_name='currency_id',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='id',
            new_name='customer_id',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='id',
            new_name='invoice_id',
        ),
        migrations.RenameField(
            model_name='invoice_detail',
            old_name='id',
            new_name='invoice_detail_id',
        ),
    ]
