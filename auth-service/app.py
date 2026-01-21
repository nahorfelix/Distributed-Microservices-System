from flask import Flask, request, jsonify
from flask_cors import CORS
import jwt
import datetime

app = Flask(__name__)
CORS(app) # Allows the React frontend to talk to this service
app.config['SECRET_KEY'] = 'tt_group_super_secret_key'

# Mock Database
users = {
    "admin@ttgroup.com": {"password": "admin123", "role": "manager"},
    "staff@ttgroup.com": {"password": "password123", "role": "employee"}
}

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users.get(data.get('email'))
    if user and user['password'] == data.get('password'):
        token = jwt.encode({
            'sub': data.get('email'),
            'role': user['role'],
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        return jsonify({'token': token, 'role': user['role']})
    return jsonify({'message': 'Invalid credentials'}), 401

if __name__ == '__main__':
    app.run(port=5001, debug=True)