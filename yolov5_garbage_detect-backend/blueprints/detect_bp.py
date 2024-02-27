import os
from pprint import pprint

from flask import Blueprint, request, render_template, g, redirect, session
from PIL import Image
import datetime
import base64

from io import BytesIO
from flask_jwt_extended import jwt_required
from database_models import WeightsModel
from utils.backend_utils.dir_utils import *
from utils.backend_utils.model_handler import load_model
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

bp = Blueprint(name='detect', import_name=__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"


@bp.route('/weights/current')
@jwt_required(refresh=True)
def get_current_weights():
    weights_path = session['weights_path']
    current_weights = WeightsModel.query.filter_by(weights_relative_path=weights_path).first()
    weights_name = current_weights.weights_name
    weights_version = current_weights.weights_version
    data = {
        'weightsName': weights_name,
        'weightsVersion': weights_version,
    }
    return response(code=0, message='获取当前调用权重成功', data=data)


@bp.route('/weights/list')
@jwt_required(refresh=True)
def get_all_enable_weights():
    all_enable_weights = []
    weights_models = WeightsModel.query.filter_by(enable=True).all()
    for weights_model in weights_models:
        all_enable_weights.append({
            'weightsName': weights_model.weights_name,
            'weightsVersion': weights_model.weights_version
        })
    data = {'list': all_enable_weights}
    return response(code=0, message='获取所有可调用权重成功', data=data)


@bp.route('/weights/switch', methods=['POST'])
@jwt_required(refresh=True)
def switch_weights():
    weights_name = request.json.get('switchWeightsName', '').strip()
    weights_version = request.json.get('switchWeightsVersion', '').strip()
    repo_dir = session['repo_dir']
    new_weights = WeightsModel.query.filter_by(weights_name=weights_name,
                                               weights_version=weights_version).first()
    if new_weights and new_weights.enable:
        new_weights_path = new_weights.weights_relative_path
        new_weights_name = new_weights.weights_name
        new_weights_version = new_weights.weights_version
        model_load_path = os.path.join(repo_dir, new_weights_path)
        print_cyan(f'切换成功，当前调用权重：{new_weights_name}，权重版本{weights_version}')
        session['repo_dir'] = repo_dir
        session['weights_path'] = new_weights_path
        session['model_load_path'] = model_load_path
        session['weights_name'] = new_weights_name
        data = {
            'weightsName': new_weights_name,
            'weightsVersion': new_weights_version,
        }
        return response(code=200, message='切换模型成功', data=data)
    elif not new_weights:
        return response(code=201, message='切换模型失败，当前模型不存在')
    else:
        return response(code=201, message='切换模型失败，当前模型暂不可用')


@bp.route('/upload', methods=['POST'])
def upload_file():
    if "file" not in request.files:
        return response(code=1, message='模型推断失败，未检测到文件')
    file = request.files["file"]
    if not file:
        return response(code=1, message='模型推断失败，未检测到文件')
    # 加载模型
    if session['weights_name'] == session['default_weights_name']:
        model = g.model
    else:
        model = load_model(repo_dir=session['repo_dir'],
                           model_load_path=session['model_load_path'])
    # 获取上传的文件
    file = request.files['file']
    # inference
    original_base64, result_base64, detect_result = inference_image(model, file)

    data = {
        'originalBase64': original_base64,
        'resultBase64': result_base64,
        'detectResult': detect_result,
    }
    return response(code=0, message='模型推断已完成', data=data)


# 模型推断-图片
def inference_image(model, file):
    img_bytes = file.read()
    img = Image.open(BytesIO(img_bytes))
    # inference
    results = model([img])
    # 处理返回检测结果
    result_df = results.pandas().xyxy[0]
    # 保留confidence列的两位小数
    result_df['confidence'] = result_df['confidence'].round(2)
    # 重命名name列为className列
    result_df = result_df.rename(columns={'name': 'className'})
    # 提取confidence和className列，转换为字典
    detect_result = result_df[['confidence', 'className']].to_dict('records')
    # 处理返回结果图片 base64编码
    results.render()  # updates results.ims with boxes and labels
    now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
    img_save_name = f"static/detect_result/{now_time}.png"
    output_dir = os.path.join(g.repo_dir, 'static/detect_result')
    create_dir(output_dir)
    Image.fromarray(results.imgs[0]).save(img_save_name)
    # base64 encoded image with results
    original_base64 = base64.b64encode(img_bytes).decode('utf-8')
    result_base64 = batch_base64_encode_image(results)
    return original_base64, result_base64, detect_result


# base64编码推断后图片
def batch_base64_encode_image(results_images):
    for im in results_images.imgs:
        buffered = BytesIO()
        im_base64 = Image.fromarray(im)
        im_base64.save(buffered, format="JPEG")
    return base64.b64encode(buffered.getvalue()).decode('utf-8')
