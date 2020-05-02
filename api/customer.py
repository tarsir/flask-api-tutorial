import random
import string

from flask import Blueprint, jsonify

from core.query import query_full_model, query_full_models
from db.models.customer import Customer
from db.database_init import get_db_instance

customer_api = Blueprint('customer', __name__)

customer_names = ["Jeff", "Bob", "Alan", "Steve"]
db = get_db_instance()

@customer_api.route('/customer/<int:customer_id>')
def get_customer(customer_id):
    customer = Customer.query.get(customer_id)
    return jsonify(query_full_model(customer))

@customer_api.route('/customers')
def customer_list():
    return jsonify(query_full_models(Customer.query.all()))

@customer_api.route('/generate_customer', methods=['POST'])
def random_customer():
    customer = Customer(
            random.choice(customer_names),
            random.choice(customer_names),
            "customer{customer_number}@example.com".format(customer_number=random.randint(1, 20)),
            ''.join([random.choice(string.digits) for i in range(10)]))
    db.session.add(customer)
    db.session.commit()
    return jsonify(customer.__dict__)

# For test purposes only
def make_test_customer(customer_number):
    customer = Customer()
    customer.name = random.choice(customer_names)
    customer.email_address = "customer{customer_number}@example.com".format(customer_number=customer_number)
    customer.phone_number = ''.join([random.choice(string.digits) for i in range(10)])
    customer.is_registered = True
    return customer
