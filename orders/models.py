from django.contrib.auth.models import User
from django.db import models



class DevicesService(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class SnacksService(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    device = models.ManyToManyField(DevicesService, null=True, blank=True)
    fullname = models.CharField(max_length=60)
    company = models.CharField(max_length=60)
    position = models.CharField(max_length=60)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField(null=True, blank=True)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    date = models.DateField()
    file = models.FileField(null=True, blank=True)
    start_time = models.TimeField()
    finish_time = models.TimeField()
    people = models.IntegerField()
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    def __str__(self):
        return self.fullname

class Quantity(models.Model):
    order = models.ForeignKey(Order,related_name='order', on_delete=models.CASCADE)
    snack = models.ForeignKey(SnacksService, on_delete=models.CASCADE)
    number = models.IntegerField()

    class Meta:
        verbose_name = "Snack"
        verbose_name_plural = "Number of Snacks"

    def __str__(self):
        return f"{self.number}"
