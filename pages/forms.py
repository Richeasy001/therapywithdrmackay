# from django import forms
# from datetime import time
# from django.core.exceptions import ValidationError
# from .models import SessionBooking

# class SessionBookingForm(forms.ModelForm):
#     # Replace time field with ChoiceField for dynamic dropdown
#     time = forms.ChoiceField(choices=[], required=True)

#     class Meta:
#         model = SessionBooking
#         fields = [
#             'first_name', 'last_name', 'phone_number',
#             'email', 'location', 'date', 'time', 'summary_complaint'
#         ]

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)

#         # Apply Bootstrap styling
#         for name, field in self.fields.items():
#             field.widget.attrs.update({'class': 'form-control'})

#         # Set HTML5 date picker for date field
#         self.fields['date'].widget.attrs.update({'type': 'date'})

#         # Time field choices will be dynamically populated via JavaScript
#         self.fields['time'].choices = []

#     def clean_time(self):
#         selected_time = self.cleaned_data['time']
#         try:
#             selected_time = time.fromisoformat(selected_time)
#         except ValueError:
#             raise ValidationError("Invalid time format.")
#         if selected_time < time(8, 0) or selected_time > time(16, 0):
#             raise ValidationError("Time must be between 8:00 AM and 4:00 PM.")
#         return selected_time

#     def clean(self):
#         cleaned_data = super().clean()
#         date = cleaned_data.get('date')
#         selected_time = cleaned_data.get('time')

#         try:
#             selected_time = time.fromisoformat(selected_time)
#         except Exception:
#             return  # Let `clean_time()` handle format issues

#         if date and selected_time:
#             if SessionBooking.objects.filter(date=date, time=selected_time).exists():
#                 raise ValidationError("This date and time slot is already booked. Please choose another.")
from django import forms
from .models import SessionBooking

class SessionBookingForm(forms.ModelForm):
    class Meta:
        model = SessionBooking
        fields = '__all__'
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
        }