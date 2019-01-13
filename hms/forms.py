from django import forms
from .models import Reservation

class ReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        exclude = ('time', 'user')

    def __init__(self, *args, **kwargs):
        super(ReservationForm, self).__init__(*args, **kwargs)

        # iterate all fields and give them a class
        for fname, f in self.fields.items():
            f.widget.attrs['class'] = 'form-control'