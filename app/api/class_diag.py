from flask import Blueprint
from . import get_data, handle_error, params_check
from ..util import trueReturn, falseReturn

class_diag_blueprint = Blueprint('class_diag_blueprint', __name__, url_prefix='/class_diag')


@class_diag_blueprint.before_request
@handle_error
def before_request():
    get_data()
