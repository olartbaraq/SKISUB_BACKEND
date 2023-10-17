# from django.contrib import admin
from skisub.models import BillOperation
# from carbook.models import  CarMake,Car,CarImage,Booking, CarModel
# from hotelbooking.models import Amenity,HotelImage,Hotel
# from hotelbooking.models import Booking as hotelbooking
# from account.models import CustomUserManager,Skisubuser





# admin.site.register(CarModel)
# admin.site.register(CarMake)
# admin.site.register(Car)
# admin.site.register(CarImage)
# admin.site.register(Booking)
# admin.site.register(Amenity)
# admin.site.register(HotelImage)
# admin.site.register(Hotel)
# admin.site.register(hotelbooking)

from django.contrib import admin
# from skisub.models import BillOperation
from carbook.models import CarMake, Car, CarImage, Booking, CarModel
from hotelbooking.models import Amenity, HotelImage, Hotel
from hotelbooking.models import Booking as hotelbooking

admin.site.register(BillOperation)
# from account.models import CustomUserManager, Skisubuser
class CarImageInline(admin.TabularInline):
    model = Car.image.through  # Through model for the ManyToMany relationship
    extra = 1

class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]  # Include CarImage inlines for easy image management
    list_display = ('model', 'year', 'available', 'price_per_day')
    list_filter = ('model__make', 'available')
    search_fields = ('model__name', 'year')
    list_editable = ('available', 'price_per_day')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'car', 'start_date', 'end_date', 'pickup_time', 'dropoff_time', 'is_approved', 'total_amount')
    list_filter = ('user', 'is_approved')
    search_fields = ('user__username', 'car__model__name')
    list_editable = ('is_approved', 'total_amount','car','start_date','end_date', 'pickup_time', 'dropoff_time')

# Register your custom admin classes with the Django admin site
admin.site.register(CarMake)
admin.site.register(CarModel)
admin.site.register(Car, CarAdmin)
admin.site.register(CarImage)
admin.site.register(Booking, BookingAdmin)

class HotelImageInline(admin.TabularInline):
    model = Hotel.images.through  # Through model for the ManyToMany relationship
    extra = 1

class AmenityAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

class HotelAdmin(admin.ModelAdmin):
    inlines = [HotelImageInline]  # Include HotelImage inlines for easy image management
    list_display = ('name', 'price_per_day', 'available', 'location')
    list_filter = ('amenities', 'available')
    search_fields = ('name', 'location')
    list_editable = ('available', 'price_per_day')

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'hotel', 'check_in_date', 'check_out_date', 'total_amount')
    list_filter = ('user', 'hotel')
    search_fields = ('user__username', 'hotel__name')

# Register your custom admin classes with the Django admin site
admin.site.register(Amenity, AmenityAdmin)
admin.site.register(Hotel, HotelAdmin)
admin.site.register(HotelImage)
admin.site.register(hotelbooking, BookingAdmin)






