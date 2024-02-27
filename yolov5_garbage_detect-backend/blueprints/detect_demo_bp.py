from flask import Blueprint, request, render_template, g, redirect, session
from PIL import Image
import datetime
import base64

from io import BytesIO

from utils.backend_utils.dir_utils import *
from utils.backend_utils.model_handler import load_model


bp = Blueprint(name='detect_demo', import_name=__name__)

DATETIME_FORMAT = "%Y-%m-%d_%H-%M-%S-%f"

# 模型推断demo
@bp.route("/upload", methods=["GET", "POST"])
def detect():
    if session['weights_name'] == session['default_weights_name']:
        model = g.model
    else:
        model = load_model(repo_dir=session['repo_dir'],
                           model_load_path=session['model_load_path'])

    if request.method == "POST":
        if "file" not in request.files:
            return redirect(request.url)

        file = request.files["file"]
        if not file:
            return

        img_bytes = file.read()
        img = Image.open(BytesIO(img_bytes))
        results = model([img])

        results.render()  # updates results.imgs with boxes and labels
        now_time = datetime.datetime.now().strftime(DATETIME_FORMAT)
        img_save_name = f"static/detect_result/{now_time}.png"
        output_dir = os.path.join(g.repo_dir, 'static/detect_result')
        create_dir(output_dir)
        Image.fromarray(results.imgs[0]).save(img_save_name)
        return redirect('/' + img_save_name)

    return render_template("index.html")