
# from datetime import date
# from django.db import models
# # from .models import Car

# class CarMake(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class CarModel(models.Model):
#     make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name
# class CarImage(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='car_images/')
    
#     def __str__(self):
#         return f'Image for {self.car}'
    
#     def get_first_image(self):
#         # Get the first image associated with the car
#         first_image = self.images.first()
#         return first_image
    
# class Car(models.Model):
#     model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
#     year = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     # start_date = models.DateField(default=date.today)
#     # end_date = models.DateField(default=date.today)
#     price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     images = models.ManyToManyField(CarImage, blank=True)
#     # image = models.ImageField(upload_to='car_images/', blank=True, null=True)

#     def __str__(self):
#         return f'{", ".join(self.makes.values_list("name", flat=True))} --- {self.model}'

# class Booking(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     start_date = models.DateField(default=date.today)
#     end_date = models.DateField(default=date.today)
#     is_approved = models.BooleanField(default=False)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f'Booking for {", ".join(self.car.makes.values_list("name", flat=True))} --- {self.car.model}'
# from datetime import date
# from django.db import models

# class CarMake(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class CarModel(models.Model):
#     make = models.ForeignKey(CarMake, on_delete=models.CASCADE, related_name='models')
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class CarImage(models.Model):
#     car = models.ForeignKey('Car', on_delete=models.CASCADE, related_name='images')
#     image = models.ImageField(upload_to='car_images/')

#     def __str__(self):
#         return f'Image for {self.car}'

# class Car(models.Model):
#     model = models.ForeignKey(CarModel, on_delete=models.CASCADE, related_name='cars')
#     year = models.PositiveIntegerField()
#     available = models.BooleanField(default=True)
#     price_per_day = models.DecimalField(max_digits=10, decimal_places=2, default=0)
#     images = models.ManyToManyField(CarImage, blank=True, related_name='cars')

#     def __str__(self):
#         return f'{self.model.make.name} --- {self.model.name}'

# class Booking(models.Model):
#     car = models.ForeignKey(Car, on_delete=models.CASCADE)
#     start_date = models.DateField(default=date.today)
#     end_date = models.DateField(default=date.today)
#     is_approved = models.BooleanField(default=False)
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

#     def __str__(self):
#         return f'Booking for {self.car.model.make.name} --- {self.car.model.name}'
from datetime import date
from django.db import models
from datetime import time

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
    pickup_time = models.TimeField()  # Set default pickup time to 8:00 AM
    dropoff_time = models.TimeField()  # Set default dropoff time to 5:00 PM
    age = models.IntegerField(default=18) 

    def __str__(self):
        return f'Booking for {self.car.model.make.name} --- {self.car.model.name}'
