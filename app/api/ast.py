from flask import Blueprint
from . import get_data, handle_error, params_check
from ..util import trueReturn, falseReturn

ast_blueprint = Blueprint('ast_blueprint', __name__, url_prefix='/ast')


@ast_blueprint.before_request
@handle_error
def before_request():
    get_data()
