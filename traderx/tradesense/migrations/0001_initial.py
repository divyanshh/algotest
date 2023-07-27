# Generated by Django 4.2.3 on 2023-07-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cryptos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('crypto_name', models.CharField(max_length=300, unique=True)),
                ('symbol', models.CharField(default='', max_length=30, unique=True)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('quote_currency_id', models.IntegerField(default=2781)),
                ('sort', models.CharField(max_length=300)),
                ('sort_direction', models.CharField(choices=[('asc', 'asc'), ('desc', 'desc')], default='desc', max_length=30)),
                ('limit', models.IntegerField(default=100)),
                ('start', models.IntegerField(default=1)),
                ('category', models.CharField(default='spot', max_length=300)),
                ('market_pair', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Exchange',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('exchange_name', models.CharField(max_length=300, unique=True)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Trades',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('crypto_name', models.CharField(max_length=300, unique=True)),
                ('slug', models.CharField(max_length=300, unique=True)),
                ('quote_currency_id', models.IntegerField(default=0)),
                ('market_pair', models.CharField(max_length=30)),
                ('buy_exchange', models.CharField(max_length=30)),
                ('sell_exchange', models.CharField(max_length=30)),
                ('buy_price', models.FloatField(default=0)),
                ('sell_price', models.FloatField(default=0)),
                ('arbitrage', models.FloatField(default=0)),
            ],
        ),
    ]
