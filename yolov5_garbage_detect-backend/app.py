import sqlalchemy
import config
import argparse
import os

from flask import Flask, g, session
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from extensions import *
from utils.backend_utils.colorprinter import *
from utils.backend_utils.model_handler import load_model

from database_models import *
from blueprints.auth_bp import bp as auth_bp
from blueprints.server_bp import bp as server_bp
from blueprints.user_manage_bp import bp as user_manage_bp
from blueprints.detect_demo_bp import bp as detect_demo_bp
from blueprints.detect_bp import bp as detect_bp

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

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
jwt = JWTManager(app)
mail.init_app(app)
'''
flask db init
flask db migrate
flask db upgrade
'''
migrate = Migrate(app, db)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(server_bp, url_prefix='/server')
app.register_blueprint(user_manage_bp, url_prefix='/user-manage')
app.register_blueprint(detect_demo_bp, url_prefix='/detect-demo')
app.register_blueprint(detect_bp, url_prefix='/detect')


# 注册一个函数，该函数在第一次请求之前运行
@app.before_first_request
def load_default_model():
    g.repo_dir = repo_dir
    # print_cyan(f'repo_dir: {repo_dir}')
    g.weights_path = weights_path
    g.model_load_path = model_load_path
    # 加载默认调用权重并保存在g.model中
    g.model = default_model
    g.weights_name = WeightsModel.query.filter_by(weights_relative_path=weights_path).first().weights_name
    # 同时把当前权重相关调用信息存储进session
    # 后续如果调用的非默认权重则重新根据session中的信息加载模型
    session['repo_dir'] = g.repo_dir
    session['weights_path'] = g.weights_path
    session['model_load_path'] = g.model_load_path
    session['weights_name'] = g.weights_name
    session['default_weights_name'] = g.weights_name


# 注册一个函数，该函数在每次请求之前运行
@app.before_request
def before_request():
    # 如果session中存储当前调用权重信息
    # 如果session中的weights_name与default_weights_name则重新加载模型
    g.repo_dir = session['repo_dir']
    g.weights_path = session['weights_path']
    g.model_load_path = session['model_load_path']
    g.weights_name = session['weights_name']
    g.model = default_model


def test_database_connection():
    with app.app_context():
        with db.engine.connect() as conn:
            res = conn.execute(sqlalchemy.text('select 1'))
            if res.fetchone()[0] == 1:
                print_green('Database connection successful')
            else:
                print_red('Database connection failed')


if __name__ == "__main__":
    repo_dir = os.getcwd()
    # weights_path = 'weights/yolov5-7.0/COCO_yolov5s6.pt'
    # weights_path = 'weights/yolov5-6.2/Sample_yolov5s6_300_epochs.pt'
    weights_path = 'weights/yolov5-3.1/TACO_yolov5s_300_epochs.pt'
    # weights_path = 'weights/yolov5-3.1/Garbage_yolov5s_300_epochs.pt'
    model_load_path = os.path.join(repo_dir, weights_path)

    parser = argparse.ArgumentParser(description="Flask app exposing yolov5 models")
    parser.add_argument("--port", default=5003, type=int, help="port number")
    args = parser.parse_args()

    # webapp启动后加载默认调用权重
    default_model = load_model(repo_dir, model_load_path)
    test_database_connection()
    print_cyan('项目已启动')
    print_cyan(f'当前工作目录: {repo_dir}')
    print_cyan(f'当前调用权重: {weights_path}')
    print_cyan(f'模型推断请访问: http://localhost:{args.port}/detect-demo/upload')

    app.run(host="0.0.0.0", port=args.port, debug=True)
