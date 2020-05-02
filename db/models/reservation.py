from db.database_init import get_db_instance
from sqlalchemy.orm import relationship


db = get_db_instance()

class Reservation(db.Model):
    __tablename__ = 'reservation'
    id = db.Column(db.Integer, primary_key=True)
    guest_count = db.Column(db.Integer)
    is_confirmed = db.Column(db.Boolean)
    is_canceled = db.Column(db.Boolean)
    time_and_date = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey("customer.id"))
    restaurant_id = db.Column(db.Integer, db.ForeignKey("restaurant.id"))

    def __repr__(self):
        return "<Reservation {}>".format(self.id)
