from django.shortcuts import render
from .models import Reservation, Restandbar
from .forms import ReservationForm, RestandbarForm


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

    all_restandbars = Restandbar.objects.all()

    if request.method == 'POST':
        form = RestandbarForm(request.POST)
        if form.is_valid():
            restandbar = form.save(commit=False)
            restandbar.user = request.user
            restandbar.save()
    
    form = RestandbarForm()
    return render(request, 'hms/restandbar.html', {'form': form, 'all_restandbars': all_restandbars})


def inventory(request):
    return render(request, 'hms/inventory.html')

def room(request):
    return render(request, 'hms/room.html')