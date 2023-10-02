from app import app, db
from flask import request,jsonify
from models import Restaurant, Pizza, RestaurantPizza

# Define your routes here
@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    formatted_restaurants = []
    for restaurant in restaurants:
        formatted_restaurants.append({
            'id': restaurant.id,
            'name': restaurant.name,
            'address': restaurant.address
        })
    return jsonify(formatted_restaurants)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    formatted_pizzas = []
    for pizza in restaurant.pizzas:
        formatted_pizzas.append({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })

    return jsonify({
        'id': restaurant.id,
        'name': restaurant.name,
        'address': restaurant.address,
        'pizzas': formatted_pizzas
    })

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if not restaurant:
        return jsonify({'error': 'Restaurant not found'}), 404

    # Delete associated RestaurantPizzas
    RestaurantPizza.query.filter_by(restaurant_id=id).delete()

    # Delete the restaurant
    db.session.delete(restaurant)
    db.session.commit()

    return '', 204

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    formatted_pizzas = []
    for pizza in pizzas:
        formatted_pizzas.append({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        })
    return jsonify(formatted_pizzas)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.json
    price = data.get('price')
    pizza_id = data.get('pizza_id')
    restaurant_id = data.get('restaurant_id')

    # Validate input data 
    if not all([price, pizza_id, restaurant_id]):
        return jsonify({'errors': ['Missing required fields']}), 400

    
    try:
        new_pizza = RestaurantPizza(price=price, pizza_id=pizza_id, restaurant_id=restaurant_id)
        db.session.add(new_pizza)
        db.session.commit()
        pizza = Pizza.query.get(pizza_id)
        return jsonify({
            'id': pizza.id,
            'name': pizza.name,
            'ingredients': pizza.ingredients
        }), 201
    except Exception as e:
        return jsonify({'errors': [str(e)]}), 400