from flask import Blueprint
from . import get_data, handle_error, params_check
from ..util import trueReturn, falseReturn

data_flow_diag_blueprint = Blueprint('data_flow_diag_blueprint', __name__, url_prefix='/data_flow_diag')


@data_flow_diag_blueprint.before_request
@handle_error
def before_request():
    get_data()
