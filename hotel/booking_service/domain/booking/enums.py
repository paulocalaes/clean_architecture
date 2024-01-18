from enum import Enum

class ErrorCodes(Enum):
    CHECKIN_AFTER_CHECKOUT = 'Checkin date cannot be after checkout'
    CUSTOMER_CANNOT_BE_BLANK = 'Customer is required'
    CUSTOMER_SHOULD_BE_OLDER_THAN_18 = 'Customer should be older than 18'
    INVALID_CUSTOMER_DOCUMENT = 'Invalid customer document'
    UNDEFINED = 'Undefined error'

class SuccessCodes(Enum):
    SUCCESS = 'Success'