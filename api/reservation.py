import random
import datetime

from flask import Blueprint, jsonify, request

from core.query import query_full_model, query_full_models
from db.database_init import get_db_instance
from db.models.reservation import Reservation
from db.models.customer import Customer
from db.models.restaurant import Restaurant

reservation_api = Blueprint('reservation', __name__)
db = get_db_instance()

@reservation_api.route('/reservations')
def reservation_list():
    return jsonify(query_full_models(Reservation.query.all()))

@reservation_api.route('/reservations/new', methods=['POST'])
def add_reservation():
    print(request.form)
    customer_id = request.form["customer_id"]
    if customer_id:
        print(Customer.query.get(customer_id))

    restaurant_id = request.form["restaurant_id"]
    if restaurant_id:
        print(Restaurant.query.get(restaurant_id))

    return "OK"
