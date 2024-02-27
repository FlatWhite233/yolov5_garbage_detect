import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired, DataRequired
from database_models import UserModel, CaptchaModel
from extensions import db
from flask import request


class LoginForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message='用户名不能为空')])
    password = wtforms.StringField(validators=[DataRequired(message='密码不能为空'),
                                               Length(min=4, max=20, message='密码字符数限制：4-20')])
    code = wtforms.StringField(validators=[DataRequired(message='验证码不能为空')])
