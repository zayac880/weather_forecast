from flask import request, jsonify
from services.database import Database
from services.weather_api import fetch_weather

db = Database()


def update_balance_route():
    # Getting the userId and city parameters from the JSON body of the request
    data = request.json
    user_id = data.get('userId')
    city = data.get('city')

    if user_id is None or city is None:
        return jsonify({'message': 'Both userId and city parameters are required.'}), 400
    # We get the current temperature in the specified city
    temperature = fetch_weather(city)

    if temperature is not None:
        # Getting the user's current balance from the database
        current_balance = db.get_balance(user_id)

        if current_balance is not None:
            # Update user balance based on temperature
            new_balance = current_balance + temperature
            if new_balance >= 0:
                db.update_balance(user_id, new_balance)
                return jsonify({'message': 'Balance updated successfully.'}), 200
            else:
                return jsonify({'message': 'Balance cannot be negative.'}), 400
        else:
            return jsonify({'message': f'User with id {user_id} not found.'}), 404
    else:
        return jsonify({'message': 'Failed to fetch weather data.'}), 500