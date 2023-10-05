from django.db import models
from account.models import Skisubuser

class Hotel(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='hotels/')  # You may need to configure MEDIA_ROOT and MEDIA_URL in settings.py
    price_per_day = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    description = models.TextField()
    location=models.CharField(max_length=255)
    amenities=models.TextField()

    def __str__(self):
        return self.name

# Model to represent hotel bookings
class Booking(models.Model):
    # user = models.ForeignKey(Skisubuser, on_delete=models.CASCADE,)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    # def save(self, *args, **kwargs):
    #     delta = self.check_out_date - self.check_in_date
    #     self.total_amount = delta.days * self.hotel.price_per_day
    #     super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.hotel.name}"
