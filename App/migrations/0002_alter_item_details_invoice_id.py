# Generated by Django 4.0.4 on 2022-05-09 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_details',
            name='invoice_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='details', to='App.invoice'),
        ),
    ]
