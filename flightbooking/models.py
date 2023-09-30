from django.db import models

class Flight(models.Model):
    # flight_name = models.CharField(max_length=200)
    departure_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    adult_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    child_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

    def __str__(self):
        return f'{self.departure_location} to {self.destination}'

class Booking(models.Model):
    TRIP_CHOICES = (
        ('one_way', 'One Way'),
        ('round_trip', 'Round Trip'),
    )

    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    trip_type = models.CharField(max_length=20, choices=TRIP_CHOICES, default='one_way')  # Add trip type field
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def save(self, *args, **kwargs):
        if self.trip_type == 'one_way':
            self.total_amount = (self.flight.adult_price * self.adults) + (self.flight.child_price * self.children)
        elif self.trip_type == 'round_trip':
            self.total_amount = 2 * (self.flight.adult_price * self.adults) + (self.flight.child_price * self.children)
        super().save(*args, **kwargs)
