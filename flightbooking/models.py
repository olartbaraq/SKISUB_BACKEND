# from datetime import date
# from django.db import models

# class Flight(models.Model):
#     TRIP_CHOICES = (
#         ('one_way', 'One Way'),
#         ('round_trip', 'Round Trip'),
#     )
#     CLASS_CHOICES = (
#         ('economy', 'economy'),
#         ('first_class', 'first_class'),
#     )
    
#     departure_location = models.CharField(max_length=100)
#     destination = models.CharField(max_length=100)
#     adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     child_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     departure_date = models.DateField(default=date.today)
#     return_date = models.DateField(default=date.today)
#     trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='one_way')
#     select_class=models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')

#     def __str__(self):
#         return f'{self.departure_location} to {self.destination}'

# class Booking(models.Model):
#     TRIP_CHOICES = (
#         ('one_way', 'One Way'),
#         ('round_trip', 'Round Trip'),
#     )
#     CLASS_CHOICES = (
#         ('economy', 'economy'),
#         ('first_class', 'first_class'),
#     )

#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     adults = models.PositiveIntegerField()
#     children = models.PositiveIntegerField()
#     departure_date = models.DateField(default=date.today)
#     return_date = models.DateField(default=date.today)
#     trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='one_way')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
#     select_class=models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')

#     def save(self, *args, **kwargs):
#         if self.trip_type == self.flight.trip_type:
#             if self.select_class==self.flight.select_class:
#                 if self.departure_date == self.flight.departure_date and self.return_date == self.flight.return_date:
#                     self.total_amount = (self.flight.adult_price * self.adults) + (self.flight.child_price * self.children)
#                 else:
#                     self.total_amount = (self.flight.adult_price * self.adults) + (self.flight.child_price * self.children)
#         super().save(*args, **kwargs)

from datetime import date
from django.db import models

class Flight(models.Model):
    TRIP_CHOICES = (
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip'),
    )
    CLASS_CHOICES = (
        ('economy', 'Economy'),
        ('first_class', 'First Class'),
    )
    
    departure_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    child_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    departure_date = models.DateField(default=date.today)
    return_date = models.DateField(default=date.today)
    trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='one_way')
    select_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')

    def __str__(self):
        return f'{self.departure_location} to {self.destination}'

class Booking(models.Model):
    TRIP_CHOICES = (
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip'),
    )
    CLASS_CHOICES = (
        ('economy', 'Economy'),
        ('first_class', 'First Class'),
    )

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    departure_date = models.DateField(default=date.today)
    return_date = models.DateField(default=date.today)
    trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='one_way')
    select_class = models.CharField(max_length=20, choices=CLASS_CHOICES, default='economy')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        # Ensure trip type and class match the flight
        if self.trip_type == self.flight.trip_type and self.select_class == self.flight.select_class:
            # Calculate the total amount based on prices and passenger counts
            self.total_amount = (self.flight.adult_price * self.adults) + (self.flight.child_price * self.children)
        super().save(*args, **kwargs)



