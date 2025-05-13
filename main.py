
from flask import Flask, jsonify, request, send_file
import os

app = Flask(__name__)

# Временное хранилище пользователей
users = {
    "946001310": {
        "name": "Александр",
        "username": "testuser",
        "rank": "E",
        "age": 24,
        "role": "Разработчик"
    }
}

@app.route("/")
def index():
    return send_file("index.html")

@app.route("/user/<string:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    user_id = data.get("telegram_id")
    if user_id in users:
        return jsonify({"error": "User already exists"}), 400
    users[user_id] = {
        "name": data.get("name"),
        "username": data.get("username"),
        "rank": data.get("rank"),
        "age": data.get("age"),
        "role": "Боец"
    }
    return jsonify({"message": "User registered successfully"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
