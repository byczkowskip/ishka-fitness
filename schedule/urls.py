from django.urls import path

from schedule import views

app_name = 'schedule'
urlpatterns = [
    path('', views.SessionListView.as_view(), name='session_list'),
    path('booking_form/', views.BookingFromView.as_view(), name='booking_form'),
]
