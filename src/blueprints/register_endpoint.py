from flask import jsonify, Blueprint, request, current_app
import datetime
from werkzeug.security import generate_password_hash
import json
import re
from ..db import get_db

col = get_db()

blueprint_register = Blueprint(name='blueprint_register', import_name=__name__)

@blueprint_register.route('/', methods=['POST'])
def register():
    try:
        if request.method == 'POST':
            user = json.loads(request.data)
            username = user['username']
            password = user['password']
            dummy = password
            email = user['email']
            password = generate_password_hash(password)
            uname = col.find_one({'username': username})
            if uname:
                return jsonify({'status': 'failure', 'error': 'Username already exists'})
            elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
                return jsonify({'status': 'failure', 'error': 'Invalid email address'})
            elif not re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', dummy):
                return jsonify({'status': 'failure',
                                'error': 'Password must contain at least 8 characters, 1 uppercase, 1 lowercase, '
                                         '1 number and 1 special character'})
            elif not re.match(r'[A-Za-z0-9]+', username):
                return jsonify({'status': 'failure', 'error': 'Username must contain only letters and numbers'})
            else:
                user_dict = {'username': username, 'email': email, 'password': password,
                             'date': datetime.datetime.now()}
                status = col.insert_one(user_dict)
                return jsonify({'status': 'success', 'id': str(status.inserted_id)})
        else:
            return jsonify({'status': 'failure', 'error': 'Invalid request'})
    except Exception as e:
        return jsonify({'status': 'failure', 'error': str(e)})


