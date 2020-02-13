from .customer import Customer
from .restaurant import Restaurant

class Reservation:
    guest_count = 1
    is_confirmed = False
    is_canceled = False
    time_and_date = None
    customer = ''
    restaurant = ''
