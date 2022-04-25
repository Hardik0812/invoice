# Generated by Django 4.0.4 on 2022-04-22 22:25

import App.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('currency_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('symbol', models.TextField(max_length=1)),
                ('name', models.CharField(max_length=20)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField(max_length=1000, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('invoice_id', models.CharField(default=App.models.Invoice.increment_invoice_number, max_length=20000, primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('paid', models.IntegerField()),
                ('note', models.TextField(max_length=1000)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('currency_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.currency')),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.customer')),
            ],
        ),
        migrations.CreateModel(
            name='Item_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sr_no', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('rate', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.invoice')),
            ],
        ),
    ]
