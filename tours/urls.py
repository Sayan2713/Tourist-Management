# tourist_management_system_project/tours/urls.py

from django.urls import path
from . import views # Import views from the current app

app_name = 'tours' # Namespace for this app's URLs

urlpatterns = [
    path('', views.tour_list, name='tour_list'), # URL for listing all tours
    path('<int:pk>/', views.tour_detail, name='tour_detail'),
    path('<int:pk>/book/', views.book_tour, name='book_tour'),
    # path('<int:pk>/', views.tour_detail, name='tour_path('my-bookings/', views.my_bookings, name='my_bookings'),detail'), # For individual tour details, will add next
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('destinations/', views.destination_list, name='destination_list'), # NEW: URL for listing destinations

]