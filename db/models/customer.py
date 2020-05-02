from db.database_init import get_db_instance
from sqlalchemy.orm import relationship


db = get_db_instance()

class Customer(db.Model):
    __tablename__ = 'customer'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(40))
    last_name = db.Column(db.String(40))
    email_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    is_registered = db.Column(db.Boolean)
    password_hash = db.Column(db.String(100))
    reservations = relationship("Reservation", backref="customer")

    def __init__(self, first_name, last_name, email_address, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email_address = email_address
        self.phone_number = phone_number
