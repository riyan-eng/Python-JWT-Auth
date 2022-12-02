from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from os import getenv

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = getenv('SECRET_KEY')

jwt = JWTManager(app)

@app.route('/login', methods=['POST'])
def login():
    payload = request.json
    user = {
        'id': 2,
        'username': 'mata',
        'password': 'we'
    }
    if payload['username'] == user['username'] and payload['password'] == user['password']:
        return jsonify({
            'status': 200,
            'data': {
                'access_token': create_access_token(identity=user)
            },
            'message': 'success'
        }), 200
    else:
        return jsonify({
            'status': 400,
            'data': 'periksa username dan password anda',
            'message': 'error'
        }), 400

@app.route('/user')
@jwt_required()
def user():

    return jsonify({
        'status': 200,
        'data': get_jwt_identity(),
        'message': 'success'
    })

@app.route('/')
def index():
    return jsonify({
        'status': 200,
        'data': '',
        'message': 'success'
    })