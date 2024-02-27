from werkzeug.security import generate_password_hash

from database_models import *
from batch_add_user import add_users
from weights_init import *


def init_role():
    with app.app_context():
        admin = RoleModel(role_name='admin', role_desc='管理员')
        user = RoleModel(role_name='user', role_desc='普通用户')
        db.session.add_all([admin, user])
        db.session.commit()


def init_user():
    with app.app_context():
        root = UserModel(email='root@gmail.com',
                         username='root',
                         password=generate_password_hash('root'),
                         role_id=1)
        admin = UserModel(email='admin@gmail.com',
                          username='admin',
                          password=generate_password_hash('admin'),
                          role_id=1)
        user = UserModel(email='user@gmail.com',
                         username='user',
                         password=generate_password_hash('user'),
                         role_id=2)
        test01 = UserModel(email='test01@gmail.com',
                         username='test01',
                         password=generate_password_hash('test'),
                         role_id=2,
                         status=True)
        test02 = UserModel(email='test02@gmail.com',
                         username='test02',
                         password=generate_password_hash('test'),
                         role_id=2,
                         status=False)
        test03 = UserModel(email='test03@gmail.com',
                         username='test03',
                         password=generate_password_hash('test'),
                         role_id=2,
                         status=False)
        db.session.add_all([root, admin, user, test01, test02, test03])
        db.session.commit()


def init_dataset():
    with app.app_context():
        COCO_dataset = DatasetModel(dataset_name='COCO',
                                    class_num=80,
                                    total_num=123287,
                                    train_num=118287,
                                    val_num=5000,
                                    test_exist=False,
                                    test_num=20288)
        Sample_dataset = DatasetModel(dataset_name='Sample',
                                      class_num=6,
                                      total_num=1200,
                                      train_num=972,
                                      val_num=108,
                                      test_num=120)
        TACO_dataset = DatasetModel(dataset_name='TACO',
                                    class_num=8,
                                    total_num=1086,
                                    train_num=869,
                                    val_num=108,
                                    test_num=109)
        Garbage_dataset = DatasetModel(dataset_name='Garbage',
                                       class_num=43,
                                       total_num=14964,
                                       train_num=12120,
                                       val_num=1347,
                                       test_num=1497)
        db.session.add_all([COCO_dataset,
                            Sample_dataset,
                            TACO_dataset,
                            Garbage_dataset])
        db.session.commit()


if __name__ == '__main__':
    init_role()
    init_user()
    init_dataset()
    init_COCO_weights()
    init_Sample_weights()
    init_TACO_weights()
    init_Garbage_weights()
    add_users(2000)
