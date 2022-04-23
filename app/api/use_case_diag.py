from flask import Blueprint, request
from flask_uploads import UploadSet, DOCUMENTS
from ..core import use_case_diag

from . import get_data, handle_error, params_check
from ..util import trueReturn, falseReturn

use_case_diag_blueprint = Blueprint('use_case_diag_blueprint', __name__, url_prefix='/use_case_diag')

#usecase是UploadSet的名字，与配置文件中相同
usecase = UploadSet('usecase', DOCUMENTS)

@use_case_diag_blueprint.before_request
@handle_error
def before_request():
    get_data()

@use_case_diag_blueprint.route('/', methods = ['POST'])
def handle():
    context = {}
    file_url = None
    print("aaa", request.files)
    # usecase是html中input的name对应的值
    if request.method == 'POST' and 'usecase' in request.files:
        # 保存文件到本地
        file_name = usecase.save(request.files['dataflow'])
        # 返回文件路径
        file_url = usecase.url(file_name)
        basename = usecase.get_basename(file_name)
        path = usecase.path(file_name)
        print('file_url = ', file_url)
        print('basename = ', basename)
        print('path = ', path)
    context[file_url] = file_url
    return use_case_diag.getActorandUseCase(path)

@use_case_diag_blueprint.route('/trial', methods = ['GET'])
def trial():
    return {'code': 200, 'msg': "Use Case Hello :)"}