# Generated by Django 2.2.6 on 2019-10-23 22:38

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('is_vegan', models.BooleanField(default=False)),
                ('is_meat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=250)),
                ('last_name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=20, unique=True)),
                ('email', models.CharField(max_length=250)),
                ('address', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('ingredients', models.ManyToManyField(to='pizza.Ingredient')),
                ('size', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pizza.Size')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('number', models.PositiveIntegerField(default=1)),
                ('cost', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('comments', models.TextField()),
                ('pizza', models.ManyToManyField(to='pizza.Pizza')),
                ('user', models.ManyToManyField(to='pizza.User')),
            ],
        ),
    ]
