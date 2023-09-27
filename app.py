
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Import your routes here
from routes import *

if __name__ == '__main__':
    with app.app_context():  # Add this line to create tables within application context
        db.create_all()
        from seed import seed_data
        seed_data()
    app.run(port=5555)
