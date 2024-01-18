from booking_service.domain.booking.exceptions import CheckinDateCannotBeAfterCheckoutDate, CustomerCannotBeBlank
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import ErrorCodes

class BookingManager(object):
    def create_new_booking(self, booking_dto: BookingDto):
        domain_object = booking_dto.to_domain()

        try:
            if domain_object.is_valid():
                return 'save'
        except CheckinDateCannotBeAfterCheckoutDate as e:
            return {'message':e.message, 'code':ErrorCodes.CHECKIN_AFTER_CHECKOUT}
        except CustomerCannotBeBlank as e:
            return {'message':e.message, 'code':ErrorCodes.CUSTOMER_CANNOT_BE_BLANK}
        except Exception as e:
            return {'message':e.message, 'code':ErrorCodes.UNDEFINED}