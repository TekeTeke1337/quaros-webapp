
from flask import Flask, jsonify, request
import json

app = Flask(__name__)

# Пример пользователей (вместо базы данных)
users = {
    "946001310": {"name": "Александр", "rank": "E", "age": 24, "role": "Разработчик", "username": "testuser"}
}

@app.route('/user/<string:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route('/register', methods=['POST'])
def register_user():
    data = request.get_json()
    user_id = data.get('telegram_id')
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = {
        "name": data.get("name"),
        "rank": data.get("rank"),
        "age": data.get("age"),
        "role": "Боец",
        "username": data.get("username")
    }
    return jsonify({"message": "User registered successfully"}), 200

@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    tournaments = [
        {"title": "Зимний турнир", "description": "Турнир на выживание", "rank": "E", "date": "2025-12-01"},
        {"title": "Летний турнир", "description": "Турнир на силу", "rank": "C", "date": "2026-06-15"}
    ]
    return jsonify(tournaments)

if __name__ == '__main__':
    app.run(debug=True)
