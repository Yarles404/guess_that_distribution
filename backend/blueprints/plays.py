from flask import Blueprint, request

plays = Blueprint('plays', __name__)

@plays.route('/api/plays', methods=['GET'])
def get_plays():
    return 'List of users sorted by play'

@plays.route('/api/plays', methods=['POST'])
def post_play():
    data = request.json
    return 'play posted'

@plays.route('/api/plays', methods=['PUT'])
def put_play():
    data = request.json
    return 'play posted'

@plays.route('/api/plays', methods=['GET'])
def get_play():
    data = request.json
    return 'play for user'

@plays.route('/api/plays', methods=['DELETE'])
def delete_play():
    data = request.json
    return 'play deleted'


