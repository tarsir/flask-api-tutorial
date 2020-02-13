import random
import datetime

from flask import Blueprint, jsonify

from db.models.reservation import Reservation

reservation_api = Blueprint('reservation', __name__)

@reservation_api.route('/reservations')
def reservation_list():
    return jsonify([reservation.__dict__ for reservation in test_reservations])

def make_test_reservation(guest_count):
    reservation = Reservation()
    reservation.guest_count = guest_count
    reservation.is_confirmed = random.randint(0, 10) % 2 == 1

    today = datetime.datetime.now()
    reservation.time_and_date = today.replace(day=today.day + 7, hour=19)
    return reservation

test_reservations = [make_test_reservation(n) for n in range(1, 6)]
print(test_reservations)
