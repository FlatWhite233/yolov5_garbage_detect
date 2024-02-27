import cv2
import torch
import os
from PIL import Image
import base64
from io import BytesIO


# repo_dir = '/Users/saber/Code/Back-end/garbage_detect-backend/'
repo_dir = 'E:/Code/Back-end/garbage_detect-backend/'
weights_path = 'weights/exp3_TACO_yolov5s_300_epochs_3090Ti/weights/best.pt'
model_path = os.path.join(repo_dir, weights_path)
yolov5s_model_path = os.path.join(repo_dir, 'weights/yolov5s.pt')

# Model
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
model = torch.hub.load(repo_dir, 'custom', path=model_path, source='local', device='cpu')
# model = torch.hub.load(repo_dir, 'custom', path=yolov5s_model_path, source='local', device='cpu')

# Images
# im1 = Image.open(os.path.join(repo_dir, 'data/images/zidane.jpg'))  # PIL image
# im2 = cv2.imread(os.path.join(repo_dir, 'data/images/bus.jpg'))[..., ::-1]  # OpenCV image (BGR to RGB)
im3 = Image.open(os.path.join(repo_dir, 'data/images/batch_1_000029.jpg'))  # PIL image


results = model(im3)  # inference

results.imgs # array of original images (as np array) passed to model for inference
results.render()  # updates results.ims with boxes and labels
for im in results.imgs:
    buffered = BytesIO()
    im_base64 = Image.fromarray(im)
    im_base64.save(buffered, format="JPEG")
    print(base64.b64encode(buffered.getvalue()).decode('utf-8'))  # base64 encoded image with results

# results.print()
# results.save()

results.xyxy[0]  # im1 predictions (tensor)
results.pandas().xyxy[0]  # im1 predictions (pandas)