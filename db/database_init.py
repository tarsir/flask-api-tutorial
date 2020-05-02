from sqlalchemy import create_engine, MetaData
from flask_sqlalchemy import SQLAlchemy


DATABASE_URL = 'postgresql://foodspot:foodspot@localhost:5433/foodspot'
SQLALCHEMY_INSTANCE = SQLAlchemy()

metadata = MetaData()
engine = create_engine(DATABASE_URL)

# NOTE: how to make sure the integration to our Flask app happens
# before we load the models?

def get_db_instance(app = None):
    if app:
        SQLALCHEMY_INSTANCE.init_app(app)
    return SQLALCHEMY_INSTANCE
