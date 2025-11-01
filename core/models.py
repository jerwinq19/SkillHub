from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Service(models.Model):
    service_name = models.CharField(max_length=300)
    service_description = models.TextField()
    price = models.IntegerField(default=0)
    provider = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user")
    status = models.BooleanField(default=True)
    slug = models.SlugField(default="", unique=True, editable=False)
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.service_name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return f"{self.service_name} - {self.service_description[:20]}"


class Transaction(models.Model):
    STATUS_CHOICES = (
        ("Pending", "Pending"),
        ("Accepted", "Accepted"),
        ("Completed", "Completed"),
        ("Cancelled", "Cancelled"),
    )
    
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="service")
    booking_owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    booking_status = models.CharField(max_length=50, choices=STATUS_CHOICES, default="Pending")
    date_issued = models.DateTimeField(auto_now_add=True, editable=True)
    
    def __str__(self):
        return f"{self.service.service_name} - {self.booking_status} - {self.booking_owner.username}"