from django.contrib import admin
from .models import Reservation


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('time', 'guest', 'room', 'user')
    list_filter = ('time', 'user')
    search_fields = ('guest',)

admin.site.register(Reservation, ReservationAdmin)