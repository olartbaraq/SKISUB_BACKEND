from datetime import date
from django.db import models

class CarMake(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarModel(models.Model):
    make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CarImage(models.Model):
    car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='car_images')  # Specify a unique related_name here
    image = models.ImageField(upload_to='car_images/')

    def __str__(self):
        return f'Image for {self.car}'

class Car(models.Model):
    model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
    year = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    image = models.ManyToManyField(CarImage, blank=True, related_name='cars_images')  # Specify a unique related_name here

    def __str__(self):
        return f'{self.model.make.name} --- {self.model.name}'

class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    start_date = models.DateField(default=date.today)
    end_date = models.DateField(default=date.today)
    is_approved = models.BooleanField(default=False)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return f'Booking for {self.car.model.make.name} --- {self.car.model.name}'
