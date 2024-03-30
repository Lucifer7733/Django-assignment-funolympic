from django.contrib import admin
from home.models import UserProfile  # Import the model associated with the SignUpForm
from .models import Video  # Import the model associated with the video/broadcast 
from .models import NewsArticle # Import the model associated with the news
from .models import Event

admin.site.register(UserProfile)  # Register the model in the admin site


admin.site.register(Video)  # Register the model in the admin site

admin.site.register(NewsArticle) # Register the model in the admin site

admin.site.register(Event) 
