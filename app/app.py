from flask import Flask
from api.user_Api import user_Api_blueprint
from api.country_city_Api import country_city_Api_blueprint
from api.place_Api import place_Api_blueprint
from api.review_Api import review_Api_blueprint
from api.amenity_Api import amenity_Api_blueprint

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development/db'
app.config['USE_DATABASE'] = True
db = SQLAlchemy(app)



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


if __name__ == "__main__":
    db.create_all()
    app.run(host='0.0.0.0', port=8000, debug=True)
