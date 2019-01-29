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


@login_required
def reservation(request):

    all_reservations = Reservation.objects.all()

    # reduce the number of objects to display
    list_num = 5
    if all_reservations.count() >= list_num:
        few_reservations = []
        for i in range(list_num):
            few_reservations.append(all_reservations[i])
        all_reservations = few_reservations

    # auto add user to form
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
    
    form = ReservationForm()
    return render(request, 'hms/reservation.html', {'form': form, 'all_reservations': all_reservations})


@login_required
def restandbar(request):

    all_restandbars = Restandbar.objects.all()

    # reduce the number of objects to display
    list_num = 5
    if all_restandbars.count() >= list_num:
        few_restandbars = []
        for i in range(list_num):
            few_restandbars.append(all_restandbars[i])
        all_restandbars = few_restandbars

    # auto add user to form
    if request.method == 'POST':
        form = RestandbarForm(request.POST)
        if form.is_valid():
            restandbar = form.save(commit=False)
            restandbar.user = request.user
            restandbar.save()

    form = RestandbarForm()
    return render(request, 'hms/restandbar.html', {'form': form, 'all_restandbars': all_restandbars})


@login_required
def inventory(request):
    return render(request, 'hms/inventory.html')


@login_required
def room(request):
    return render(request, 'hms/room.html')
