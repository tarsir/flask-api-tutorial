from flask import Flask, jsonify
from flask_cors import CORS

from api.customer import customer_api
from api.restaurant import restaurant_api
from core import response

class JsonDefaultFlask(Flask):
    response_class = response.JsonResponse

app = JsonDefaultFlask(__name__)
CORS(app)
app.register_blueprint(customer_api)
app.register_blueprint(restaurant_api)

@app.route("/")
def hello():
    return "I'm alive!"

if __name__ == '__main__':
    app.run()
