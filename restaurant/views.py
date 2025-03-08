from django.http import JsonResponse
from django.shortcuts import render
from .models import Booking
from datetime import datetime

def booking_form(request):
    today = datetime.today().strftime('%Y-%m-%d')
    return render(request, 'restaurant/booking_form.html', {'today': today})

def reservations(request):
    date = request.GET.get('date')
    if date:
        bookings = Booking.objects.filter(reservation_date=date)
        if bookings.exists():
            data = list(bookings.values('first_name', 'reservation_date', 'reservation_slot'))
            return JsonResponse(data, safe=False)
        return JsonResponse({'message': 'No Booking'}, status=404)
    return JsonResponse({'message': 'Invalid Date'}, status=400)
