# tourist_management_system_project/tours/admin.py

from django.contrib import admin
from .models import Destination, TourPackage, Booking, Review # Import your models

# Register your models here so they appear in the Django admin site.
admin.site.register(Destination)
admin.site.register(TourPackage)
#admin.site.register(Booking)
admin.site.register(Review)

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'tour_package', 'booking_date', 'number_of_people',
        'total_price', 'status', 'payment_status', 'payment_id', 'payment_method' # Add new fields here
    )
    list_filter = ('status', 'payment_status', 'booking_date')
    search_fields = ('user__username', 'tour_package__name', 'payment_id')
    readonly_fields = ('booking_date', 'total_price') # These are calculated or auto-set