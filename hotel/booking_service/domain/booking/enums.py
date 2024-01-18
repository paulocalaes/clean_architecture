from enum import Enum

class ErrorCodes(Enum):
    CHECKIN_AFTER_CHECKOUT = 'Checkin date cannot be after checkout'
    CUSTOMER_CANNOT_BE_BLANK = 'Customer is required'
    UNDEFINED = 'Undefined error'