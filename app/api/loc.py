from flask import Blueprint, request
from werkzeug.datastructures import FileStorage

from . import get_data, handle_error
from ..core import loc

loc_blueprint = Blueprint('loc_blueprint', __name__, url_prefix='/loc')


# @loc_blueprint.before_request
# @handle_error
# def before_request():
#     get_data()


@loc_blueprint.route('/loc', methods=['POST'])
def handle():
    if request.method == 'POST':
        a: FileStorage = request.files.get('file')
        b = a.stream.readlines()
        return loc.getLCOM(b)
    else:
        return None

# 测试用
@loc_blueprint.route('/hello')
def hello():
    return {'code': 200, 'data': "success! :)"}
