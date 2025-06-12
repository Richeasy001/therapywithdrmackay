from datetime import datetime
from django.db import models

class SessionBooking(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=25)
    email = models.EmailField()
    location = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    subject = models.CharField(max_length=255)
    summary = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('date', 'time')  # Prevent double booking

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.date} at {self.time}"