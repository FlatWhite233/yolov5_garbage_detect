from extensions import db
from datetime import datetime


class UserModel(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='用户id')
    username = db.Column(db.String(100), nullable=False, comment='用户名')
    password = db.Column(db.String(500), nullable=False, comment='密码')
    email = db.Column(db.String(100), nullable=False, unique=True, comment='邮箱')
    join_time = db.Column(db.DateTime, default=datetime.now, comment='加入时间')
    status = db.Column(db.Boolean, default=True, comment='是否启用')
    # ForeignKey 默认注册为普通用户
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'), default=2, comment='用户角色')
    # Relationship
    roles = db.relationship('RoleModel', backref=db.backref('users', lazy='dynamic'))

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'createTime': self.join_time.strftime('%Y-%m-%d %H:%M:%S'),
            'status': self.status,
            'roles': self.roles.role_name,
        }


class RoleModel(db.Model):
    __tablename__ = 'role'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='角色id')
    role_name = db.Column(db.String(100), nullable=False, comment='角色名称')
    role_desc = db.Column(db.String(100), nullable=False, comment='角色描述')


class CaptchaModel(db.Model):
    __tablename__ = 'captcha'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), nullable=True, comment='验证邮箱')
    captcha = db.Column(db.String(100), nullable=False, comment='验证码')
    create_time = db.Column(db.DateTime, default=datetime.now, comment='创建时间')
    is_used = db.Column(db.Boolean, default=False, comment='是否使用')


class DatasetModel(db.Model):
    __tablename__ = 'dataset'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='数据集id')
    dataset_name = db.Column(db.String(100), nullable=False, comment='数据集名称')
    class_num = db.Column(db.Integer, nullable=False, comment='类别数量')
    total_num = db.Column(db.Integer, nullable=False, comment='总数量')
    train_num = db.Column(db.Integer, nullable=False, comment='训练集数量')
    val_num = db.Column(db.Integer, nullable=False, comment='验证集数量')
    test_exist = db.Column(db.Boolean, default=True, nullable=False, comment='是否存在测试集')
    test_num = db.Column(db.Integer, nullable=True, comment='测试集数量')


class ImageModel(db.Model):
    __tablename__ = 'image'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='图片id')
    image_name = db.Column(db.String(100), nullable=False, comment='图片名称')
    image_absolute_path = db.Column(db.Text, nullable=True, comment='图片绝对路径')
    image_relative_path = db.Column(db.Text, nullable=True, comment='图片相对路径')
    image_type = db.Column(db.String(100), nullable=False, comment='图片类型')
    # ForeignKey
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))
    # Relationship
    dataset = db.relationship('DatasetModel', backref=db.backref('image'))


class LabelModel(db.Model):
    __tablename__ = 'label'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='标注id')
    label_name = db.Column(db.String(100), nullable=False, comment='标注名称')
    # ForeignKey
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))
    # Relationship
    dataset = db.relationship('DatasetModel', backref=db.backref('label'))


class ImageLabelInfoModel(db.Model):
    __tablename__ = 'image_label_info'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='图片标注信息id')
    # ForeignKey
    image_id = db.Column(db.Integer, db.ForeignKey('image.id'), comment='图片id')
    label_id = db.Column(db.Integer, db.ForeignKey('label.id'), comment='标注id')
    # Relationship
    image = db.relationship('ImageModel', backref=db.backref('image_label_info'))
    label = db.relationship('LabelModel', backref=db.backref('image_label_info'))


class WeightsModel(db.Model):
    __tablename__ = 'weights'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='权重id')
    weights_name = db.Column(db.String(100), nullable=False, comment='权重名称')
    weights_relative_path = db.Column(db.Text, nullable=False, comment='权重相对路径')
    weights_absolute_path = db.Column(db.Text, nullable=True, comment='权重绝对路径')
    weights_version = db.Column(db.String(100), nullable=False, comment='权重版本')
    enable = db.Column(db.Boolean, default=False, nullable=False, comment='是否启用')
    # ForeignKey
    dataset_id = db.Column(db.Integer, db.ForeignKey('dataset.id'))
    # Relationship
    dataset = db.relationship('DatasetModel', backref=db.backref('weights'))


class DetectResultModel(db.Model):
    __tablename__ = 'detect_result'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, comment='检测结果id')
    detect_result = db.Column(db.Text, nullable=False, comment='检测结果')
    detect_result_image_name = db.Column(db.String(100), nullable=False, comment='检测结果图片名称')
    detect_time = db.Column(db.DateTime, default=datetime.now, comment='检测时间')
    # ForeignKey
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # Relationship
    user = db.relationship('UserModel', backref=db.backref('detect_result'))
