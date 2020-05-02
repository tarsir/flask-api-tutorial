import random
import string
from flask import Blueprint, jsonify

from core.query import query_full_model, query_full_models
from db.models.restaurant import Restaurant
from db.database_init import get_db_instance

restaurant_api = Blueprint('restaurant', __name__)

adjectives = ['Delicious', 'Marvelous', 'Exemplary', 'Glorious']
db = get_db_instance()

@restaurant_api.route('/restaurant/<int:restaurant_id>')
def get_restaurant(restaurant_id):
    return jsonify(query_full_model(Restaurant.query.get(restaurant_id)))

@restaurant_api.route('/restaurants')
def list_restaurants():
    return jsonify(query_full_models(Restaurant.query.all()))

@restaurant_api.route('/generate_restaurant', methods=['POST'])
def random_restaurant():
    restaurant = Restaurant()
    restaurant.name = random.choice(adjectives) + " Meats"
    restaurant.seat_count = random.randint(10, 24)
    restaurant.average_table_time = random.randint(5, 150)
    restaurant.email_address = "restaurant{restaurant_number}@example.com".format(restaurant_number=random.randint(1, 20))
    restaurant.phone_number = ''.join([random.choice(string.digits) for i in range(10)])
    db.session.add(restaurant)
    db.session.commit()
    return jsonify(query_full_model(restaurant))

# test data
def make_test_restaurant():
    restaurant = Restaurant()
    restaurant.name = random.choice(adjectives) + " Meats"
    restaurant.seat_count = random.randint(10, 24)
    restaurant.average_table_time = random.randint(5, 150)
    return restaurant
