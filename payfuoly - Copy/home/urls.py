from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
        path('', views.home, name='home'),
        path('schedule/', views.schedule, name='schedule'),
        path('broadcast/', views.broadcast, name='broadcast'),
         path('news/', views.news, name='news'),
        path('signup', views.signup, name='signup'),
        path('signin', views.signin, name='signin'),
        path('add_event/', views.add_event, name='add_event'),
        path('edit_event/<int:event_id>/', views.edit_event, name='edit_event'),
        path('delete_event/<int:event_id>/', views.delete_event, name='delete_event'),
        path('signout', views.signout, name='signout'),
]
