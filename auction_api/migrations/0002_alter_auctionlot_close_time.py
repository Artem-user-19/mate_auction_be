# Generated by Django 5.1.4 on 2024-12-15 09:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("auction_api", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="auctionlot",
            name="close_time",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 12, 22, 9, 0, 40, 635850, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
