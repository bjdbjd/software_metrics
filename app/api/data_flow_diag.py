from flask import Blueprint, request, render_template
from flask_uploads import UploadSet, DOCUMENTS
from ..core import data_flow_diag
from . import get_data, handle_error, params_check
from ..util import trueReturn, falseReturn

data_flow_diag_blueprint = Blueprint('data_flow_diag_blueprint', __name__, url_prefix='/data_flow_diag')

#dataflow是UploadSet的名字，与配置文件中相同
dataflow = UploadSet('dataflow', DOCUMENTS)

@data_flow_diag_blueprint.before_request
@handle_error
def before_request():
    get_data()

@data_flow_diag_blueprint.route('/', methods=['POST'])
def handle():
    context = {}
    file_url = None
    print("aaa", request.files)
    #data_flow是html中input的name标签对应的值
    if request.method == 'POST' and 'dataflow' in request.files:
        # 保存文件到本地
        file_name = dataflow.save(request.files['dataflow'])
        # 返回文件路径
        file_url = dataflow.url(file_name)
        basename = dataflow.get_basename(file_name)
        path = dataflow.path(file_name)
        print('file_url = ', file_url)
        print('basename = ', basename)
        print('path = ', path)
    context['file_url'] = file_url
    return data_flow_diag.getMcCabe(path)

@data_flow_diag_blueprint.route('/hello')
def hello():
    return {'code':200, 'data': "success! :)"}