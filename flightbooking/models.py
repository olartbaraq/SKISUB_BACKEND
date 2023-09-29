from django.db import models
import flightbooking


class Flight(models.Model):
    departure_location = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

# class Booking(models.Model):
#     flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
#     adults = models.IntegerField()
#     children = models.IntegerField()
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2)

# models.py


class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)  # Assuming you have a Flight model
    adults = models.PositiveIntegerField()
    children = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Define the DecimalField here with a default value

    def save(self, *args, **kwargs):
        # Calculate total_amount based on flight price, adults, and children
        self.total_amount = (self.flight.price * self.adults) + (self.flight.price * self.children)
        super().save(*args, **kwargs)


