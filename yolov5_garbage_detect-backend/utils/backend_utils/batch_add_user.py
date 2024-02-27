import random
import string

from app import app
from extensions import db
from database_models import UserModel, RoleModel


def generate_password(length=8):
    """生成随机密码"""
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(length))


def add_users(num):
    """批量添加用户"""
    with app.app_context():
        for i in range(1, num+1):
            username = f"工具人{i}号"
            password = generate_password()
            email = f"user{i}@example.com"
            user_role = random.choice(RoleModel.query.all())
            user_status = random.choice([True, False])
            user = UserModel(username=username, password=password, email=email, roles=user_role, status=user_status)
            db.session.add(user)
        db.session.commit()


if __name__ == '__main__':
    add_users(2000)
