# Generated by Django 5.0.4 on 2024-06-07 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0008_order_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_shipped',
            field=models.BooleanField(blank=True, null=True),
        ),
    ]