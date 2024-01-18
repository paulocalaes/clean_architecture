import unittest
from datetime import datetime, timedelta
import sys
sys.path.append('..')
sys.path.append('../..')

from application.booking.booking_manager import BookingManager
from application.booking.booking_dto import BookingDto
from application.customers.customer_dto import CustomerDto

from application.booking.booking_storage import BookingStorage

class DummyStorage(BookingStorage):
    def save_booking(self, bookingDto: BookingDto):
        return True


class BookingManagerTests(unittest.TestCase):
    def __init__(self, methodName: str = ...) -> None:
        self.dummy_storage = DummyStorage()
        super().__init__(methodName)

    def test_customer_should_be_older_thn_18(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("MyCustomer", 17, "12345678901", "a@a.com")
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'CUSTOMER_SHOULD_BE_OLDER_THAN_18')

    def test_customer_document_should_be_valid(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("MyCustomer", 18, "123", "a@a.com")
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'INVALID_CUSTOMER_DOCUMENT')

    def test_create(self):
        checkin = datetime.today()
        checkout = datetime.today()
        customer = CustomerDto("MyCustomer", 18, "12345678901", "a@a.com")
        booking_dto = BookingDto(checkin=checkin, checkout=checkout, customer=customer)
        manager = BookingManager(self.dummy_storage)
        res = manager.create_new_booking(booking_dto)
        self.assertEqual(res['code'], 'SUCCESS')

if __name__ == '__main__':
    unittest.main()