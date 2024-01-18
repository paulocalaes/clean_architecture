from booking_service.domain.booking.exceptions import *
from booking_service.domain.customers.exceptions import *
from .booking_dto import BookingDto
from booking_service.domain.booking.enums import *
from .booking_storage import BookingStorage

class BookingManager(object):

    def __init__(self, storage: BookingStorage) -> None:
        self.storage = storage

    def create_new_booking(self, booking_dto: BookingDto):
        booking_aggregate = booking_dto.to_domain()
        
        try:
            booking_aggregate.create_booking()
            final_dto = booking_dto.to_dto(booking_aggregate)
            self.storage.save_booking(final_dto)
            return {'message': SuccessCodes.SUCCESS.value, 'code': SuccessCodes.SUCCESS.name}
        except CheckinDateCannotBeAfterCheckoutDate as e:
            return {'message':ErrorCodes.CHECKIN_AFTER_CHECKOUT.value, 'code':ErrorCodes.CHECKIN_AFTER_CHECKOUT.name}
        except CustomerCannotBeBlank as e:
            return {'message':ErrorCodes.CUSTOMER_CANNOT_BE_BLANK.value, 'code':ErrorCodes.CUSTOMER_CANNOT_BE_BLANK.name}
        except CustomerShouldBeOlderThan18 as e:
            return {'message': ErrorCodes.CUSTOMER_SHOULD_BE_OLDER_THAN_18.value, 'code': ErrorCodes.CUSTOMER_SHOULD_BE_OLDER_THAN_18.name}
        except InvalidCustomerDocumentException as e:
            return {'message':ErrorCodes.INVALID_CUSTOMER_DOCUMENT.value, 'code':ErrorCodes.INVALID_CUSTOMER_DOCUMENT.name}
        except Exception as e:
            return {'message':ErrorCodes.UNDEFINED.value, 'code':ErrorCodes.UNDEFINED}