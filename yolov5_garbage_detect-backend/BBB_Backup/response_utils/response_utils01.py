from flask import jsonify


def response(code=200, message='', data=None):
    """
    自定义返回结果的封装函数
    :param code: 状态码，默认为 200
    :param message: 提示信息，默认为空字符串
    :param data: 返回数据，默认为 None
    :return: Response 对象
    """
    response_data = {
        'code': code,
        'message': message,
        'data': data
    }
    return jsonify(response_data)
