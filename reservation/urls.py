from django.urls import path
from .views import MakeReservationView, ReservationConfirmationView

urlpatterns = [
    path('make/', MakeReservationView.as_view(), name='make_reservation'),
    path('confirmation/<int:reservation_id>/', ReservationConfirmationView.as_view(), name='reservation_confirmation'),
]