from django.shortcuts import render
from .models import Reservation
from .forms import ReservationForm


def dashboard(request):
    return render(request, 'hms/dashboard.html')

def reservation(request):

    all_reservations = Reservation.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
    
    form = ReservationForm()
    return render(request, 'hms/reservation.html', {'form': form, 'all_reservations': all_reservations})

def restandbar(request):
    return render(request, 'hms/restandbar.html')

def inventory(request):
    return render(request, 'hms/inventory.html')

def room(request):
    return render(request, 'hms/room.html')