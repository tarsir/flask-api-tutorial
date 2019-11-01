import random
import string

from flask import Blueprint, jsonify

from db.models.customer import Customer

customer_api = Blueprint('customer', __name__)

customer_names = ["Jeff", "Bob", "Alan", "Steve"]

@customer_api.route('/customer/<int:customer_id>')
def get_customer(customer_id):
    # return str(test_customers[customer_id]) if customer_id < len(test_customers) else ''
    return jsonify(test_customers[customer_id].__dict__) if customer_id < len(test_customers) else ''

@customer_api.route('/customers')
def customer_list():
    return jsonify([customer.__dict__ for customer in test_customers])

# For test purposes only
def make_test_customer(customer_number):
    customer = Customer()
    customer.name = random.choice(customer_names)
    customer.email_address = "customer{customer_number}@example.com".format(customer_number=customer_number)
    customer.phone_number = ''.join([random.choice(string.digits) for i in range(10)])
    customer.is_registered = True
    return customer

test_customers = [make_test_customer(num) for num in range(0, 5)]
