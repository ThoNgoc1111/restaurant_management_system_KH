from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('accounts/', include('customers.urls')),  # For registration and other account-related views
    path('orders/', include('orders.urls')),  # For the orders app
    path('reservations/', include('reservation.urls')),  # For the reservations app
    path('payments/', include('payment_processor.urls')),  # For the payments app
    # path('statistics/', include('statistics.urls')),  # For the statistics app
    # path('notifications/', include('notifications.urls')),  # For the notifications app
    path('', home, name='home'),
]