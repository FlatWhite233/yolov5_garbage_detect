import random
import string
from pprint import pprint

from flask import Blueprint, render_template, jsonify, redirect, url_for, request, session
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity, create_refresh_token
from extensions import db, mail
from flask_mail import Message
from utils.backend_utils.colorprinter import *
from database_models import CaptchaModel, UserModel
from werkzeug.security import generate_password_hash, check_password_hash
from blueprints.froms.login_form import LoginForm
from blueprints.froms.register_form import RegisterForm
from utils.backend_utils.response_utils import response

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

# /auth
bp = Blueprint('auth', __name__, url_prefix='/auth')


# 获取登陆验证码
@bp.route('/login/captcha', methods=['GET'])
def get_login_captcha():
    # 生成验证码
    captcha = ''.join(random.sample(string.ascii_letters + string.digits, 5))
    # 将验证码保存在session中
    # 默认情况下 Flask将session数据存储在服务器端的内存
    print_cyan(f'登录验证码:{captcha}')
    session['captcha'] = captcha
    code_url = f'https://dummyimage.com/100x40/dcdfe6/000000.png&text={captcha}'
    return response(code=0, data=code_url, message='获取验证码成功')


@bp.route('/register/captcha', methods=['GET', 'POST'])
def get_register_captcha():
    # /captcha/email/<email> 方法中需要接受参数 def get_register_captcha(email)
    # /captcha/email?email=xxx@qq.com
    if request.method == 'POST':
        email = request.form.get('email')
    elif request.method == 'GET':
        email = request.args.get('email')
    else:
        email = None
    # 验证当前邮箱是否被注册 在注册时后端表单将会再次验证
    user = UserModel.query.filter_by(email=email).first()
    if user is None:
        if email != '' and email is not None:
            # 4/6位 随机数字、字母、数字字母组合
            # string.digits*4:0123456789012345678901234567890123456789
            # source = string.digits*4
            # captcha = random.sample(source, 4)
            # captcha = ''.join(captcha)
            # captcha = random.randint(10000, 99999)
            captcha = ''.join(random.sample(string.ascii_letters + string.digits, 5))
            # I/O操作 耗费时间长 实际开发使用队列任务
            message = Message(subject='基于深度学习算法的垃圾检测系统验证码',
                              recipients=[email],
                              body=f'您的验证码：{captcha}')
            # 📮发送邮件📮
            mail.send(message)
            # memcached/redis存储验证码较为合适 这里使用数据库存储验证码
            email_captcha = CaptchaModel(email=email, captcha=captcha)
            db.session.add(email_captcha)
            db.session.commit()
            # RESTful API
            # {"code": 200/400/500, "message": "", "data": {}}
            return response(code=200, message='验证码已发送')
        else:
            return response(code=201, message='邮箱不能为空')
    else:
        return response(code=202, message='该邮箱已经被注册')


@bp.route('/user/login', methods=['POST'])
def login():
    json_data = request.get_json()
    # 获取表单数据
    form = LoginForm(request.form, data=json_data)
    captcha = session.get('captcha')
    # 后端校验通过
    if form.validate():
        username = form.username.data
        password = form.password.data
        user_captcha = form.code.data
        # 验证码校验
        if captcha and user_captcha == captcha:
            user = UserModel.query.filter_by(username=username).first()
            # 用户是否存在
            if not user:
                return response(code=201, message='用户不存在请先注册')
            # 用户是否被禁用
            if not user.status:
                return response(code=201, message='用户已被禁用，请联系管理员')
            # 用户名密码校验
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                # 在Flask-JWT-Extended中，create_access_token()函数用于创建一个包含用户身份信息的JWT访问令牌。
                # 访问令牌通常用于验证客户端的身份，并允许客户端访问受保护的资源。访问令牌通常具有较短的过期时间，需要经常更新或刷新。
                # 创建访问令牌：create_access_token()
                # 创建刷新令牌：create_refresh_token()
                refresh_token = create_refresh_token(identity=user.id)
                data = {'token': refresh_token}
                print_cyan('登陆成功')
                return response(code=200, data=data, message='登陆成功')
            else:
                print_cyan('用户名或密码错误')
                return response(code=201, message='用户名或密码错误')
        else:
            print_cyan('验证码错误')
            return response(code=201, message='验证码错误')
    else:
        # 后端校验失败
        msg = list(form.errors.values())[0][0]
        print_cyan(f'后端校验失败 {msg}')
        return response(code=201, message=f'后端校验失败 {msg}')


# GET：从服务器获取数据
# POST：将客户端的数据提交给服务器
@bp.route('/user/register', methods=['POST'])
def register():
    json_data = request.get_json()
    form = RegisterForm(request.form, data=json_data)
    if form.validate():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        user = UserModel(username=username,
                         password=generate_password_hash(password),
                         email=email)
        session['user_id'] = user.id
        # 注册后生成Token并返回 前端实现注册后自动登录
        refresh_token = create_refresh_token(identity=user.id)
        data = {'token': refresh_token}
        db.session.add(user)
        db.session.commit()
        print_cyan('注册成功')
        return response(code=200, data=data, message="注册成功")
    else:
        msg = list(form.errors.values())[0][0]
        print_cyan(f'后端校验失败 {msg}')
        return response(code=201, message=f'后端校验失败 {msg}')


@bp.route('/user/info', methods=['GET'])
@jwt_required(refresh=True)
def get_user_info():
    user_id = get_jwt_identity()
    user = UserModel.query.filter_by(id=user_id, status=True).first()
    if user:
        data = {
            'username': user.username,
            'email': user.email,
            'roles': [user.roles.role_name],
            'join_time': user.join_time.strftime('%Y-%m-%d %H:%M:%S')
        }
        return response(code=0, data=data, message='获取用户信息成功')
    else:
        return response(code=201, message='获取用户信息失败')


@bp.route('/switch/role', methods=['POST'])
@jwt_required(refresh=True)
def switch_role():
    role = request.json.get('role', '').strip()
    if role == 'admin':
        admin = UserModel.query.filter_by(username='admin', status=True).first()
        refresh_token = create_refresh_token(identity=admin.id)
        data = {
            'username': admin.username,
            'roles': [admin.roles.role_name],
            'token': refresh_token
        }
        return response(code=0, data=data, message='成功切换Admin权限')
    elif role == 'user':
        user = UserModel.query.filter_by(username='user', status=True).first()
        refresh_token = create_refresh_token(identity=user.id)
        data = {
            'username': user.username,
            'roles': [user.roles.role_name],
            'token': refresh_token
        }
        return response(code=0, data=data, message='成功切换User权限')
    else:
        return response(code=201, message='切换权限失败')


# http://localhost:5003/auth/mail/test
@bp.route('/mail/test')
def mail_test():
    message = Message(subject='Flask发送邮件测试',
                      recipients=['1030078310@qq.com'],
                      body='Flask发送邮件测试')
    # Windows下Flask报错提示
    # UnicodeEncodeError: 'ascii' codec can't encode characters in position 52-55: ordinal not in range(128)
    # 解决方案：https://www.cnblogs.com/Flat-White/p/17261697.html
    mail.send(message)
    return '邮件发送成功'
