from django.shortcuts import render
from .models import Reservation, Restandbar
from .forms import ReservationForm, RestandbarForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    # reservation profit
    reservation_profit = 0
    for entry in Reservation.objects.all():
        if entry.is_reservation_today():
            reservation_profit += entry.price
    # restandbar profit
    restandbar_profit = 0
    for entry in Restandbar.objects.all():
        if entry.is_restandbar_today():
            restandbar_profit += entry.price
    # total profit
    hotel_profit = reservation_profit + restandbar_profit

    # total entries
    total_sales = Reservation.objects.all().count() + Restandbar.objects.all().count()

    context = {
        'hotel_profit': hotel_profit,
        'total_sales': total_sales
    }

    return render(request, 'hms/dashboard.html', context)

def reservation(request):

    all_reservations = Reservation.objects.all()

    # auto add user to form
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