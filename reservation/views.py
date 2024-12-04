from django.shortcuts import render, redirect
from django.views import View
from core.models import MenuItem, Order, OrderItem, Reservation
from django.contrib import messages

# Create your views here.

class MakeReservationView(View):
    def get(self, request):
        return render(request, 'reservation/reservation.html')

    def post(self, request):
        date = request.POST.get('date')
        time = request.POST.get('time')
        guests = request.POST.get('guests')
        special_requests = request.POST.get('special_requests')

        reservation = Reservation.objects.create(
            user=request.user,
            date=date,
            time=time,
            guests=guests,
            special_requests=special_requests
        )

        messages.success(request, "Reservation made successfully.")
        return redirect('reservation_confirmation', reservation_id=reservation.id)
    
    
class ReservationConfirmationView(View):
    def get(self, request, reservation_id):
        reservation = Reservation.objects.get(id=reservation_id)
        return render(request, 'reservation/reservation_confirmation.html', {'reservation': reservation})