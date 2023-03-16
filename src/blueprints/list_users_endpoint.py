from flask import Blueprint, jsonify, request, current_app
from functools import wraps
import jwt
from bson import ObjectId
from ..db import get_db

col = get_db()


blueprint_list_users = Blueprint(name='blueprint_list_users', import_name=__name__)


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            data = jwt.decode(token, current_app.config['SECRET_KEY'], algorithms=["HS256"])
            current_user = col.find_one({'_id': ObjectId(data['_id'])})
        except Exception as e:
            return jsonify({'message': 'Token is invalid!', 'error': str(e)}), 401
        return f(current_user, *args, **kwargs)

    return decorated

@blueprint_list_users.route('/', methods=['GET'])
@token_required
def get_all_users(current_user):
    if not current_user:
        return jsonify({'message': 'Cannot perform that function!'})
    users = col.find()
    output = []
    for user in users:
        user_data = {}
        user_data['username'] = user['username']
        output.append(user_data)
    return jsonify({'users': output})