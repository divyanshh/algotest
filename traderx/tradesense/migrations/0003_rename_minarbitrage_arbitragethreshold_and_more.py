# Generated by Django 4.2.3 on 2023-07-27 20:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("tradesense", "0002_minarbitrage_trades_min_arbitrage_trades_success"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="MinArbitrage",
            new_name="ArbitrageThreshold",
        ),
        migrations.RenameField(
            model_name="arbitragethreshold",
            old_name="arbitrage_amount",
            new_name="arbitrage_threshold_amount",
        ),
    ]
