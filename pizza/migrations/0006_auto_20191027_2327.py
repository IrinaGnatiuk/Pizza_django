# Generated by Django 2.2.6 on 2019-10-27 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0005_auto_20191027_2253'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='number',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ManyToManyField(to='pizza.Pizza'),
        ),
    ]