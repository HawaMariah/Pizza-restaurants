# Pizza-restaurants
## Table of Contents
Installation
Usage
Configuration
Contributing
License

## Installation
To run this project on your local machine, follow these steps:

- Clone the Repository:
git clone https://github.com/yourusername/pizza-restaurant.git
cd pizza-restaurant
- Install Dependencies
- Database Setup:
This project uses SQLite as the database. No additional setup is required.
- Run the Application:
python app.py

The application will be running on http://localhost:5555.

## Usage
- View Restaurants and Pizzas:
- Get a Specific Pizza:
To get information about a specific pizza, use the endpoint: http://localhost:5555/pizzas/{id}, where {id} is the ID of the pizza.


## Acknowledgments

This project makes use of the following open-source libraries:

- [Flask](https://flask.palletsprojects.com/): A micro web framework for Python.
- [SQLAlchemy](https://www.sqlalchemy.org/): A SQL toolkit and Object-Relational Mapping (ORM) system.
- [Flask-Migrate](https://flask-migrate.readthedocs.io/): A Flask extension for database migrations.
- [Postman](https://www.postman.com/): A popular API testing tool used during development.

