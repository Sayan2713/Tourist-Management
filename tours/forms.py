

from django import forms
from .models import Booking, TourPackage, Review # Import your Booking and TourPackage models

class BookingForm(forms.ModelForm):
    # We want to show how many people are being booked
    number_of_people = forms.IntegerField(min_value=1, initial=1,
                                        help_text="Number of people for this tour.")

    class Meta:
        model = Booking
        fields = ['number_of_people', 'special_requests'] # Only allow these fields to be entered by user

    def __init__(self, *args, **kwargs):
        self.tour_package = kwargs.pop('tour_package', None) # Get tour_package from kwargs
        super().__init__(*args, **kwargs)

        # Add custom validation for available slots
        self.fields['number_of_people'].widget.attrs['max'] = self.tour_package.available_slots if self.tour_package else 1

    def clean_number_of_people(self):
        num_people = self.cleaned_data.get('number_of_people')
        if self.tour_package and num_people > self.tour_package.available_slots:
            raise forms.ValidationError(f"Only {self.tour_package.available_slots} slots available.")
        return num_people
    

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']
        widgets = {
            'comment': forms.Textarea(attrs={'rows': 4}), # Make the comment box larger
        }