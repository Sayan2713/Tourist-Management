
from django.db import models
from django.contrib.auth.models import User # For Booking and Review models

class Destination(models.Model):
    name = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='destinations/', blank=True, null=True)
    best_time_to_visit = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name

class TourPackage(models.Model):
    TOUR_TYPES = [
        ('adventure', 'Adventure'),
        ('cultural', 'Cultural'),
        ('wildlife', 'Wildlife'),
        ('beach', 'Beach'),
        ('historical', 'Historical'),
        ('family', 'Family'),
        ('spiritual', 'Spiritual'),
    ]

    name = models.CharField(max_length=255)
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='tour_packages')
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    duration_days = models.IntegerField(help_text="Duration in days")
    tour_type = models.CharField(max_length=50, choices=TOUR_TYPES, default='cultural')
    max_participants = models.IntegerField(default=10)
    available_slots = models.IntegerField(default=10)
    start_date = models.DateField()
    end_date = models.DateField()
    includes = models.TextField(blank=True, null=True, help_text="What's included in the package")
    excludes = models.TextField(blank=True, null=True, help_text="What's not included in the package")
    image = models.ImageField(upload_to='tour_packages/', blank=True, null=True)

    def __str__(self):
        return f"{self.name} to {self.destination.name}"

    def save(self, *args, **kwargs):
        if not self.available_slots:
            self.available_slots = self.max_participants
        super().save(*args, **kwargs)


class Booking(models.Model):
    BOOKING_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    PAYMENT_STATUS_CHOICES = [
        ('unpaid', 'Unpaid'),
        ('paid', 'Paid'),
        ('refunded', 'Refunded'),
        ('failed', 'Failed'), # Added 'failed' for completeness
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='bookings')
    booking_date = models.DateTimeField(auto_now_add=True)
    number_of_people = models.IntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES, default='pending')

    # Corrected payment fields - payment_status appears ONLY ONCE here
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='unpaid')
    payment_id = models.CharField(max_length=100, blank=True, null=True, help_text="Transaction ID from payment gateway")
    payment_method = models.CharField(max_length=50, blank=True, null=True, help_text="e.g., 'Credit Card', 'PayPal'")
    payment_timestamp = models.DateTimeField(blank=True, null=True, help_text="Time payment was processed")

    special_requests = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Booking for {self.user.username} on {self.tour_package.name}"

    def calculate_total_price(self):
        return self.number_of_people * self.tour_package.price

    def save(self, *args, **kwargs):
        if not self.total_price:
            self.total_price = self.calculate_total_price()
        super().save(*args, **kwargs)

class Review(models.Model):
    RATING_CHOICES = [
        (1, '1 - Poor'),
        (2, '2 - Fair'),
        (3, '3 - Good'),
        (4, '4 - Very Good'),
        (5, '5 - Excellent'),
    ]

    tour_package = models.ForeignKey(TourPackage, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(choices=RATING_CHOICES)
    comment = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('tour_package', 'user')

    def __str__(self):
        return f"{self.rating} stars for {self.tour_package.name} by {self.user.username}"