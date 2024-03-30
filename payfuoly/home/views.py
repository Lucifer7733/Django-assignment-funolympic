from django.shortcuts import render, redirect, get_object_or_404
from .forms import SignUpForm, LoginForm
from .models import Video
from .models import NewsArticle
from .models import Event
from .forms import EventForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm


def home(request):
    # Check if the user is authenticated
    if request.user.is_authenticated:
        # If authenticated, pass the user's first name to the template
        firstname = request.user.first_name
        return render(request, 'home.html', {'firstname': firstname})
    else:
        # If not authenticated, render the home page without user-specific data
        return render(request, 'home.html')
    
def broadcast(request):
    user = request.user
    if user.is_authenticated:

    # context = {'game': 'Football', 'length': '120 min'}
        videos = Video.objects.all()
        return render(request, 'broadcast.html', {'videos': videos})
    else:
        return redirect('signin')

def schedule(request):
    events = Event.objects.all()
    return render(request, 'schedule.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = EventForm()
    return render(request, 'add_event.html', {'form': form})

def edit_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('schedule')
    else:
        form = EventForm(instance=event)
    return render(request, 'edit_event.html', {'form': form})

def delete_event(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('schedule')
    return render(request, 'delete_event.html', {'event': event})

def news(request):
    news_articles = NewsArticle.objects.all()
    return render(request, 'news.html', {'news_articles': news_articles})

# def signup(request):
#     if request.method == 'POST':
#         form = SignUpForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)  # Log in the user after successful sign up
#             return redirect('home')
#     else:
#         form = SignUpForm()
#     return render(request, 'signup.html', {'form': form})

# def login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(request, username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('home')
#             else:
#                 messages.error(request, 'Invalid username or password')
#         else:
#             messages.error(request, 'Invalid form submission')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
def signup(request):
    if request.method == 'POST':
        print('inside POST method')
        form = SignUpForm(request.POST)
        if form.is_valid():
            # If the form is valid, save the user and redirect to the login page
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('signin')  # Redirect to the login page after successful signup
        else:
            # Form is not valid, render signup page with form and errors
            return render(request, 'signup.html', {'form': form, 'errors': form.errors})
    else:
        # If request method is GET, render the empty signup form
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect('home')  # Replace 'home' with the name of your home page URL pattern
        else:
            # Return an 'invalid login' error message.
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    else:
        return render(request, 'login.html')

def signout(request):
    # Log out the user and display a success message
    logout(request)
    messages.success(request, "You have been logged out successfully")
    return redirect('home')