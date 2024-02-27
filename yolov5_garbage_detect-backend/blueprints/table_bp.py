from flask import Blueprint, request
from werkzeug.security import generate_password_hash

from database_models import *
from flask_jwt_extended import jwt_required

from extensions import db
from utils.backend_utils.response_utils import response
from utils.backend_utils.colorprinter import *

'''
前后端code约定：
code: 0 成功 前端无消息弹窗
code: 1 失败 前端无消息弹窗
code: 200 前端消息弹窗Success
code: 201 前端消息弹窗Error
code: 202 前端消息弹窗Warning
code: 203 前端消息弹窗Info
code: 204 前端通知弹窗Success
code: 205 前端通知弹窗Error
code: 206 前端通知弹窗Warning
code: 207 前端通知弹窗Info
'''

bp = Blueprint('table', __name__, url_prefix='/table')


@bp.route('/list', methods=['GET'])
@jwt_required(refresh=True)
def get_users():
    page = int(request.args.get('currentPage', 1))
    per_page = int(request.args.get('size', 10))
    username = request.args.get('username', '').strip()
    email = request.args.get('email', '').strip()
    query = UserModel.query
    if username:
        query = query.filter(UserModel.username.ilike(f'%{username}%'))
    if email:
        query = query.filter(UserModel.email.ilike(f'%{email}%'))
    pagination = query.paginate(page=page, per_page=per_page, error_out=False)
    users = pagination.items
    total = pagination.total
    data = {
        'list': [user.to_dict() for user in users],
        'total': total,
    }
    return response(code=0, data=data, message='获取用户列表成功')


@bp.route('/add', methods=['POST'])
@jwt_required(refresh=True)
def add_user():
    username = request.json.get('username', '').strip()
    password = request.json.get('password', '').strip()
    email = request.json.get('email', '').strip()
    roles = request.json.get('roles', '').strip()
    if not username or not email or not password:
        return response(code=1, message='添加失败，缺少必要参数')
    user = UserModel.query.filter_by(email=email).first()
    if user is not None:
        return response(code=1, message='添加失败，用户邮箱已存在')
    roles = RoleModel.query.filter_by(role_name=roles).first()
    user = UserModel(username=username,
                     email=email,
                     password=generate_password_hash(password),
                     roles=roles)
    db.session.add(user)
    db.session.commit()
    return response(code=0, message='添加用户成功')


@bp.route('/delete/<int:user_id>', methods=['DELETE'])
@jwt_required(refresh=True)
def delete_user(user_id):
    user = UserModel.query.get(user_id)
    if user is None:
        return response(code=1, message='删除失败，用户不存在')
    db.session.delete(user)
    db.session.commit()
    return response(code=0, message='删除用户成功')


@bp.route('/update', methods=['PUT'])
@jwt_required(refresh=True)
def update_user():
    user_id = request.json.get('id', '')
    username = request.json.get('username', '').strip()
    email = request.json.get('email', '').strip()
    status = request.json.get('status', '')
    roles = request.json.get('roles', '').strip()
    if not username or not email:
        return response(code=1, message='修改失败，缺少必要参数')
    user = UserModel.query.get(user_id)
    role_id = RoleModel.query.filter_by(role_name=roles).first().id
    user.username = username
    user.email = email
    user.status = status
    user.role_id = role_id
    db.session.commit()
    return response(code=0, message='修改用户成功')
