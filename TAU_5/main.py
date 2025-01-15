from flask import Flask, request, jsonify, abort

app = Flask(__name__)


users = [
    {"id": 1, "name": "Jan Kowalski", "email": "jan@kowalski.pl"},
    {"id": 2, "name": "Anna Nowak", "email": "anna@nowak.pl"}
]


def find_user(user_id):
    return next((user for user in users if user["id"] == user_id), None)


@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users), 200


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")
    return jsonify(user), 200


@app.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data or not data.get("name") or not data.get("email"):
        abort(400, description="Invalid input")
    new_id = max(user["id"] for user in users) + 1 if users else 1
    new_user = {"id": new_id, "name": data["name"], "email": data["email"]}
    users.append(new_user)
    return jsonify(new_user), 201


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")
    data = request.json
    if not data or not data.get("name") or not data.get("email"):
        abort(400, description="Invalid input")
    user.update({"name": data["name"], "email": data["email"]})
    return jsonify(user), 200


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = find_user(user_id)
    if not user:
        abort(404, description="User not found")
    users.remove(user)
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
