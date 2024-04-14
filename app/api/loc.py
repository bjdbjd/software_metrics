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


@loc_blueprint.route('/software-estimates', methods=['POST'])
def software_estimates():
    if request.method == 'POST':
        data = request.get_json()

        # 从请求数据中获取功能点计数
        ei_simple = int(data.get('simple', 0))
        ei_average = int(data.get('average', 0))
        ei_complex = int(data.get('complex', 0))

        # 定义转换因子和其他参数
        loc_per_fp = 50  # 假设每功能点50行代码
        person_month_per_kloc = 3  # 假设每KLoC需要3人月
        cost_per_person_month = 5000  # 假设每人月成本为5000美元

        # 计算总功能点数
        total_fp = ei_simple * 3 + ei_average * 4 + ei_complex * 6

        # 计算LoC
        loc = total_fp * loc_per_fp

        # 计算工作量（人月）
        work_months = (loc / 1000) * person_month_per_kloc

        # 计算成本
        cost = work_months * cost_per_person_month

        return {
            'loc': round(loc, 2),
            'workMonths': round(work_months, 2),
            'cost': round(cost, 2)
        }
    else:
        return None


# 测试用
@loc_blueprint.route('/hello')
def hello():
    return {'code': 200, 'data': "success! :)"}
