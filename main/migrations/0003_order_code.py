# Generated by Django 3.1.2 on 2020-10-10 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_order_timing'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='code',
            field=models.CharField(max_length=100, null=True),
        ),
    ]