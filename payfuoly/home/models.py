# myapp/models.py
from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add any additional fields you want for your user profile

    def __str__(self):
        return self.user.username
    
class Video(models.Model):
    title = models.CharField(max_length=100)
    url = models.URLField()

    def __str__(self):
        return self.title

class NewsArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    image_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Event(models.Model):
    SPORT_CHOICES = [
        ('Basketball', 'Basketball'),
        ('Football', 'Football'),
        ('Tennis', 'Tennis'),
        ('Swimming', 'Swimming'),
    ]

    date = models.DateField()
    time = models.TimeField()
    event = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sport = models.CharField(max_length=100, choices=SPORT_CHOICES)

    def __str__(self):
        return f"{self.event} - {self.date}"
