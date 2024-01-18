from django.shortcuts import render
from datetime import datetime, timedelta
from booking_service.application.booking.booking_manager import BookingManager
from booking_service.application.booking.booking_dto import BookingDto
from booking_service.application.customers.customer_dto import CustomerDto
# Create your views here.

def home(request):
    customer_dto = CustomerDto()
    customer_dto.name = "Jhon Doe"
    dto = BookingDto(datetime.today(), datetime.today() - timedelta(days=1), customer_dto)
    res = BookingManager().create_new_booking(dto)
    return render(request, 'index.html', {'res': res})

def create_new(request):
    checkin = datetime.strptime(request.POST.get('checkin'), '%Y-%m-%dT%H:%M')
    checkout = datetime.strptime(request.POST.get('checkout'), '%Y-%m-%dT%H:%M')

    name = request.POST.get('name')
    age = int(request.POST.get('age'))
    document = request.POST.get('document')
    email = request.POST.get('email')
    customer_dto = CustomerDto(name=name, age=age, document=document, email=email)
    dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer_dto)
    res = BookingManager().create_new_booking(dto)

    if res['code'] != 'SUCCESS':
        return render(request, 'index.html', {'res': res})
    else:
        return render(request, 'confirmation.html')