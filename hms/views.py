from django.shortcuts import render, redirect
from .models import Reservation, Restandbar
from .forms import ReservationForm, RestandbarForm
from django.contrib.auth.decorators import login_required


@login_required
def dashboard(request):

    # reservation profit for the day
    reservation_entries = 0
    reservation_profit = 0
    for entry in Reservation.objects.all():
        if entry.is_reservation_today():
            reservation_profit += entry.price
            reservation_entries += 1

    # restandbar profit for the day
    restandbar_entries = 0
    restandbar_profit = 0
    for entry in Restandbar.objects.all():
        if entry.is_restandbar_today():
            restandbar_profit += entry.price
            restandbar_entries += 1

    # total profit
    hotel_profit = reservation_profit + restandbar_profit

    # total entries
    total_sales = reservation_entries + restandbar_entries

    context = {
        'hotel_profit': hotel_profit,
        'total_sales': total_sales,
        'section': 'dashboard',
    }

    return render(request, 'hms/dashboard.html', context)


@login_required
def reservation(request):

    all_reservations = Reservation.objects.all()

    # reduce the number of objects to display
    list_num = 7
    if all_reservations.count() >= list_num:
        few_reservations = []
        for i in range(list_num):
            few_reservations.append(all_reservations[i])
        all_reservations = few_reservations

    # collect input from form and auto add user to the form
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.user = request.user
            reservation.save()
            return redirect('reservation')

    form = ReservationForm()

    context = {
        'section': 'reservation',
        'form': form,
        'all_reservations': all_reservations,
    }

    return render(request, 'hms/reservation.html', context)


@login_required
def restandbar(request):

    all_restandbars = Restandbar.objects.all()

    # reduce the number of objects to display
    list_num = 7
    if all_restandbars.count() >= list_num:
        few_restandbars = []
        for i in range(list_num):
            few_restandbars.append(all_restandbars[i])
        all_restandbars = few_restandbars

    # collect input from form and auto add user to the form
    if request.method == 'POST':
        form = RestandbarForm(request.POST)
        if form.is_valid():
            restandbar = form.save(commit=False)
            restandbar.user = request.user
            restandbar.save()
            return redirect('restandbar')

    form = RestandbarForm()

    context = {
        'section': 'restandbar',
        'form': form,
        'all_restandbars': all_restandbars,
    }
    return render(request, 'hms/restandbar.html', context)


@login_required
def inventory(request):
    context = {
        'section': 'inventory'
    }
    return render(request, 'hms/inventory.html', context)


@login_required
def room(request):
    return render(request, 'hms/room.html')
