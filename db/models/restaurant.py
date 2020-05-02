from db.database_init import get_db_instance
from sqlalchemy.orm import relationship


db = get_db_instance()

class Restaurant(db.Model):
    __tablename__ = 'restaurant'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    city = db.Column(db.String(50))
    state = db.Column(db.String(50))
    email_address = db.Column(db.String(100))
    phone_number = db.Column(db.String(15))
    seat_count = db.Column(db.Integer)
    average_table_time = db.Column(db.Integer)
    reservations = relationship("Reservation", backref="restaurant")

    def __repr__(self):
        return "<Restaurant {}>".format(self.name)
