# tourist_management_system_project/tours/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q # For search functionality
from .models import TourPackage, Booking, Destination, Review # Ensure all models are imported
from .forms import BookingForm, ReviewForm # Ensure all forms are imported

# --- Public-facing Views ---

def home(request):
    return render(request, 'home.html')

def tour_list(request):
    tours = TourPackage.objects.all()
    query = request.GET.get('q')

    if query:
        tours = tours.filter(
            Q(name__icontains=query) |
            Q(description__icontains=query) |
            Q(destination__name__icontains=query)
        ).distinct()

    context = {
        'tours': tours,
        'query': query
    }
    return render(request, 'tours/tour_list.html', context)

def tour_detail(request, pk):
    tour = get_object_or_404(TourPackage, pk=pk)
    reviews = tour.reviews.all().order_by('-date_posted')

    review_form = None
    user_has_reviewed = False

    if request.user.is_authenticated:
        if Review.objects.filter(tour_package=tour, user=request.user).exists():
            user_has_reviewed = True
            messages.info(request, "You have already submitted a review for this tour.")
        else:
            if request.method == 'POST' and 'review_submit' in request.POST:
                review_form = ReviewForm(request.POST)
                if review_form.is_valid():
                    review = review_form.save(commit=False)
                    review.tour_package = tour
                    review.user = request.user
                    review.save()
                    messages.success(request, 'Your review has been submitted!')
                    return redirect('tours:tour_detail', pk=tour.pk)
                else:
                    messages.error(request, 'Please correct the errors in your review.')
            else:
                review_form = ReviewForm()

    context = {
        'tour': tour,
        'reviews': reviews,
        'review_form': review_form,
        'user_has_reviewed': user_has_reviewed,
    }
    return render(request, 'tours/tour_detail.html', context)

# --- Authenticated User Views (Booking & My Bookings) ---

@login_required
def book_tour(request, pk):
    tour = get_object_or_404(TourPackage, pk=pk)

    # Prevent booking if no slots
    if tour.available_slots <= 0:
        messages.error(request, f'Sorry, {tour.name} is fully booked!')
        return redirect('tours:tour_detail', pk=tour.pk)

    if request.method == 'POST':
        form = BookingForm(request.POST, tour_package=tour)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.tour_package = tour
            booking.total_price = booking.calculate_total_price()
            booking.save()

            tour.available_slots -= booking.number_of_people
            tour.save()

            messages.success(request, f'Your booking for {tour.name} has been confirmed!')
            return redirect('tours:my_bookings')
        else:
            messages.error(request, 'Please correct the errors in the form.')
    else:
        form = BookingForm(tour_package=tour)

    context = {
        'tour': tour,
        'form': form
    }
    return render(request, 'tours/book_tour.html', context)

@login_required
def my_bookings(request):
    user_bookings = Booking.objects.filter(user=request.user).order_by('-booking_date')
    context = {
        'user_bookings': user_bookings
    }
    return render(request, 'tours/my_bookings.html', context)


def destination_list(request): # NEW: View for listing destinations
    destinations = Destination.objects.all().order_by('name') # Fetch all destinations
    context = {
        'destinations': destinations
    }
    return render(request, 'tours/destination_list.html', context)