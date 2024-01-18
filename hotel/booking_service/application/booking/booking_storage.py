from abc import ABC, abstractmethod
from .booking_dto import BookingDto

class BookingStorage(ABC):
    
    @abstractmethod
    def save_booking(self, bookingDto: BookingDto):
        pass