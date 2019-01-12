import datetime
from django.db import models


class Reservation(models.Model):
    ROOM_CHOICES = (
        ('single', 'Single'),
        ('double', 'Double'),
        ('family', 'Family'),
    )
    PAYMENT_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    )
    time = models.DateTimeField(auto_now_add=True)
    guest = models.CharField(max_length=100)
    room = models.CharField(max_length=20, choices=ROOM_CHOICES)
    price = models.IntegerField()
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    remark = models.CharField(max_length=100)


    def __str__(self):
        return 'Reservation for {}'.format(self.guest)
    

    class Meta:
        ordering = ('-time',)