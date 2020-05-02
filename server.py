from flask import Flask, jsonify
from flask_cors import CORS

from core import response
from db.database_init import get_db_instance


class JsonDefaultFlask(Flask):
    response_class = response.JsonResponse

app = JsonDefaultFlask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://foodspot:foodspot@localhost:5433/foodspot'
CORS(app)

get_db_instance(app)

from api.customer import customer_api
from api.restaurant import restaurant_api
from api.reservation import reservation_api

app.register_blueprint(customer_api)
app.register_blueprint(restaurant_api)
app.register_blueprint(reservation_api)

@app.route("/")
def hello():
    return 200

if __name__ == '__main__':
    app.run()
