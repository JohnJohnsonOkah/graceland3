from django.contrib import admin
from .models import Reservation, Restandbar


class ReservationAdmin(admin.ModelAdmin):
    list_display = ('time', 'guest', 'room', 'user')
    list_filter = ('time', 'user')
    search_fields = ('guest',)


admin.site.register(Reservation, ReservationAdmin)


class RestandbarAdmin(admin.ModelAdmin):
    list_display = ('time', 'guest', 'menu_item', 'user')
    list_filter = ('time', 'user')
    search_fields = ('guest',)


admin.site.register(Restandbar, RestandbarAdmin)


admin.site.site_header = "Graceland Admin"
admin.site.site_title = "Graceland Admin Portal"
admin.site.index_title = "Welcome to Graceland Admin Portal"
