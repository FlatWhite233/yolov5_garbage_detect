import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired, DataRequired
from database_models import UserModel, CaptchaModel
from extensions import db


class RegisterForm(wtforms.Form):
    username = wtforms.StringField(validators=[DataRequired(message='用户名不能为空'),
                                               Length(min=2, max=20, message='用户名字符数限制：2-20')])
    email = wtforms.StringField(validators=[Email(message='邮箱格式错误')])
    captcha = wtforms.StringField(validators=[DataRequired(message='验证码不能为空')])
    password = wtforms.StringField(validators=[DataRequired(message='密码不能为空'),
                                               Length(min=4, max=20, message='密码字符数限制：4-20')])
    confirm_password = wtforms.StringField(validators=[EqualTo('password', message='两次输入密码不一致')])

    # 验证邮箱是否已经被注册
    def validate_email(self, filed):
        email = filed.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message='该邮箱已经被注册')

    # 验证验证码是否正确
    def validate_captcha(self, filed):
        captcha = filed.data
        email = self.email.data
        captcha_model = CaptchaModel.query.filter_by(email=email, captcha=captcha).first()
        if not captcha_model:
            raise wtforms.ValidationError('邮箱或验证码错误')
        else:
            # 可以删掉已验证的captcha_model
            # 但是每次使用完就删可能会降低服务器性能
            # db.session.delete(captcha_model)
            # 逻辑删除 设置已使用字段为True
            captcha_model.is_used = True
            db.session.commit()

    """
    Validate the form by calling ``validate`` on each field.
    Returns ``True`` if validation passes.

    If the form defines a ``validate_<fieldname>`` method, it is
    appended as an extra validator for the field's ``validate``.

    :param extra_validators: A dict mapping field names to lists of
        extra validator methods to run. Extra validators run after
        validators passed when creating the field. If the form has
        ``validate_<fieldname>``, it is the last extra validator.
    """
