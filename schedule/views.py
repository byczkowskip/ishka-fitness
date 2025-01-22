from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, FormView

from schedule.forms import BookingForm
from schedule.models import Session


class SessionListView(ListView):
    def get(self, request: HttpRequest) -> HttpResponse:
        sessions = Session.objects.all()
        return render(request,
                      'schedule/list.html',
                      {'sessions': sessions})


class BookingFromView(FormView):
    form_class = BookingForm
    template_name = 'schedule/form.html'

    def form_valid(self, form: BookingForm):
        pass