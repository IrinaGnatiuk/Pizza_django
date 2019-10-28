# Generated by Django 2.2.6 on 2019-10-27 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pizza', '0004_auto_20191027_2249'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='number',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.RemoveField(
            model_name='order',
            name='pizza',
        ),
        migrations.AddField(
            model_name='order',
            name='pizza',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='pizza.Pizza'),
        ),
    ]
