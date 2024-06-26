from flask import Flask
from api.user_Api import user_Api_blueprint
from api.country_city_Api import country_city_Api_blueprint
from api.place_Api import place_Api_blueprint
from api.review_Api import review_Api_blueprint
from api.amenity_Api import amenity_Api_blueprint
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development/db'



app.register_blueprint(user_Api_blueprint)
app.register_blueprint(country_city_Api_blueprint)
app.register_blueprint(place_Api_blueprint)
app.register_blueprint(review_Api_blueprint)
app.register_blueprint(amenity_Api_blueprint)

@app.route('/')
def hello_world():
    """
    A simple function that returns a greeting message.

    Returns:
        str: The greeting message.
    """
    return 'Hello, World!'
db = "sqlite:///development/db"
engine = create_engine(db)
Base.metadata.create_all(engine)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
