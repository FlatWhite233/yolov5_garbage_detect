from flask import Blueprint, session
from utils.backend_utils.response_utils import response
from utils.backend_utils.colorprinter import *


bp = Blueprint('server', __name__, url_prefix='/server')


# 查看服务端Session
@bp.route('/session/list', methods=['GET'])
def session_data():
    print_cyan(session)
    return response(code=200, data=session, message='获取session成功')


# 清除服务端Session
@bp.route('/session/clear')
def logout():
    session.clear()
    return response(code=200, message='清除session成功')
