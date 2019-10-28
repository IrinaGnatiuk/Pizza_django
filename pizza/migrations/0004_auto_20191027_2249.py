# Generated by Django 2.2.6 on 2019-10-27 20:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0003_auto_20191027_2233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='customer',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pizza.Customer'),
        ),
    ]
