from flask import jsonify
from sqlalchemy.orm import DeclarativeMeta


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
        'data': None
    }
    try:
        response_data['data'] = serialize(data)
        return jsonify(response_data)
    except SerializationError as e:
        response_data['code'] = e.code
        response_data['message'] = e.message
        return jsonify(response_data)


def serialize(obj):
    """
    将对象转换为可以序列化为JSON的数据类型
    :param obj: 待转换的对象
    :return: 转换后的数据类型
    """
    if obj is None:
        return None
    try:
        # 如果对象本身就是可以序列化为JSON的类型，则直接返回
        if isinstance(obj, (str, int, float, bool, list, tuple, dict)):
            return obj
        # 如果对象是ORM对象，则将其转换为字典并返回
        elif isinstance(obj.__class__, DeclarativeMeta):
            return {c.name: getattr(obj, c.name) for c in obj.__table__.columns}
        # 如果对象实现了__dict__方法，则将其转换为字典并返回
        elif hasattr(obj, '__dict__'):
            return obj.__dict__
        # 如果对象是其他类型，则抛出异常
        else:
            raise SerializationError(code=500, message='Cannot serialize object')
    except Exception as e:
        raise SerializationError(code=500, message=str(e))


class SerializationError(Exception):
    """
    自定义的异常类，用于处理序列化错误
    """
    def __init__(self, code, message):
        self.code = code
        self.message = message
