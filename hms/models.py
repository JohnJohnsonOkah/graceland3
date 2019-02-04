import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Reservation(models.Model):
    ROOM_CHOICES = (
        ('comfort 1', 'Comfort 1'),
        ('comfort 2', 'Comfort 2'),
        ('comfort 3', 'Comfort 3'),
        ('standard', 'Standard'),
        ('superior', 'Superior'),
        ('standard superior', 'Standard Superior '),
        ('classic superior', 'Classic Superior'),
        ('executives suites', 'Executives Suites'),
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
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Reservation for {}'.format(self.time)
    
    def is_reservation_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('-time',)


class Restandbar(models.Model):
    PAYMENT_CHOICES = (
        ('paid', 'Paid'),
        ('pending', 'Pending'),
    )
    time = models.DateTimeField(auto_now_add=True)
    guest = models.CharField(max_length=100)
    menu_item = models.CharField(max_length=100)
    price = models.IntegerField()
    payment_status = models.CharField(max_length=20, choices=PAYMENT_CHOICES)
    remark = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return 'Restandbar for {}'.format(self.time)

    def is_restandbar_today(self):
        return self.time >= timezone.now() - datetime.timedelta(days=1)

    class Meta:
        ordering = ('-time',)
