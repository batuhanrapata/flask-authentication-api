from flask import jsonify, Blueprint

import datetime
from datetime import timezone

blueprint_health_check = Blueprint(name='blueprint_health_check', import_name=__name__)

@blueprint_health_check.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'success', 'message': 'OK', 'timestamp': datetime.datetime.now(timezone.utc)})