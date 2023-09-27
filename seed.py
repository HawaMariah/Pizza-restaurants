
from app import db, app
from models import Restaurant, Pizza, RestaurantPizza

def seed_data():
    with app.app_context():
        db.create_all()

        # Add your seed data here
        restaurant1 = Restaurant(name="KFC", address="Town Moi Avenue")
        restaurant2 = Restaurant(name="Maveric", address="Syokimau")
        restaurant3 = Restaurant(name="Pizza Palace", address="123 Main Street")
        restaurant4 = Restaurant(name="Bella Italia", address="456 Oak Avenue")

        pizza1 = Pizza(name="Cheese", ingredients="Dough, Tomato Sauce, Cheese")
        pizza2 = Pizza(name="Pepperoni", ingredients="Dough, Tomato Sauce, Cheese, Pepperoni")
        pizza3 = Pizza(name="Margherita", ingredients="Dough, Tomato Sauce, Cheese, Basil")
        pizza4 = Pizza(name="Vegetarian", ingredients="Dough, Tomato Sauce, Cheese, Bell Peppers, Mushrooms, Olives")


        restaurant_pizza1 = RestaurantPizza(price=5, pizza=pizza1, restaurant=restaurant1)
        restaurant_pizza2 = RestaurantPizza(price=7, pizza=pizza2, restaurant=restaurant1)
        restaurant_pizza3 = RestaurantPizza(price=8, pizza=pizza3, restaurant=restaurant3)
        restaurant_pizza4 = RestaurantPizza(price=9, pizza=pizza4, restaurant=restaurant2)


        db.session.add_all([restaurant1, restaurant2, restaurant3, restaurant4, pizza1, pizza2, pizza3, pizza4, restaurant_pizza1, restaurant_pizza2, restaurant_pizza3, restaurant_pizza4])
        db.session.commit()
