from flask import Blueprint, jsonify, request,current_app
import json
from werkzeug.security import check_password_hash
import jwt
from ..db import get_db

col = get_db()

blueprint_login = Blueprint(name='blueprint_login', import_name=__name__)

@blueprint_login.route('/', methods=['POST'])  
def login():
    try:
        if request.method == 'POST':
            user = json.loads(request.data)
            username = user['username']
            password = user['password']
            uname = col.find_one({'username': username})
            if uname:
                if check_password_hash(uname['password'], password):
                    token = jwt.encode({'_id': str(uname['_id'])}, current_app.config['SECRET_KEY'])
                    return jsonify({'status': 'success', 'id': str(uname['_id']), 'access_token': token})
            else:
                return jsonify({'status': 'failure', 'error': 'Invalid username or password'})
        else:
            return jsonify({'status': 'failure', 'error': 'Invalid request'})
    except Exception as e:
        return jsonify({'status': 'failure', 'error': str(e)})

