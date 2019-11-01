import random
from flask import Blueprint, jsonify

from db.models.restaurant import Restaurant

restaurant_api = Blueprint('restaurant', __name__)

adjectives = ['Delicious', 'Marvelous', 'Exemplary', 'Glorious']

@restaurant_api.route('/restaurants')
def list_restaurants():
    return jsonify([restaurant.__dict__ for restaurant in test_restaurants])

# test data
def make_test_restaurant():
    restaurant = Restaurant()
    restaurant.name = random.choice(adjectives) + " Meats"
    restaurant.seat_count = random.randint(10, 24)
    restaurant.average_table_time = random.randint(5, 150)
    return restaurant

test_restaurants = [make_test_restaurant() for i in range(1, 3)]