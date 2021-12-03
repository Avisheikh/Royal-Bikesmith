# Generated by Django 3.2.5 on 2021-12-03 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcard',
            name='grand_total',
        ),
        migrations.AddField(
            model_name='customer',
            name='grand_total',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
    ]
