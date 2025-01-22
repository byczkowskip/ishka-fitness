from django import forms

from schedule.models import Session


class BookingForm(forms.Form):
    session = forms.ModelChoiceField(queryset=Session.objects.all())