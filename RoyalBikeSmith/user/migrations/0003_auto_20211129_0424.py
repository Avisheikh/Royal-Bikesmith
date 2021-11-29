# Generated by Django 3.2.5 on 2021-11-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20211124_2207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobcard',
            name='remarks',
        ),
        migrations.AddField(
            model_name='jobcard',
            name='grand_total',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='jobcard',
            name='invoice_no',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]