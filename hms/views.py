from django.shortcuts import render

def dashboard(request):
    return render(request, 'hms/dashboard.html')

def reservation(request):
    return render(request, 'hms/reservation.html')

def restandbar(request):
    return render(request, 'hms/restandbar.html')

def inventory(request):
    return render(request, 'hms/inventory.html')

def room(request):
    return render(request, 'hms/room.html')