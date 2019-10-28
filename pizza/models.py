from django.db import models
from django.utils import timezone
# Create your models here.


class Customer(models.Model):
    first_name = models.CharField(max_length=250, null=False)
    last_name = models.CharField(max_length=250, null=False)
    phone = models.CharField(max_length=20, null=False, unique=True, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    address = models.CharField(max_length=500, null=False)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Size(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name


class Ingredient(models.Model):
    name = models.CharField(max_length=250)
    is_vegan = models.BooleanField(default=False)
    is_meat = models.BooleanField(default=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=250)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.name


class Order(models.Model):
    date = models.DateTimeField(default=timezone.now)
    customer = models.ForeignKey(Customer,  on_delete=models.CASCADE, default=None)
    pizza = models.ManyToManyField(Pizza)
    number = models.PositiveIntegerField(default=1)
    cost = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    comments = models.TextField(default=None, blank=True)













