import cv2
import torch
import os
from PIL import Image

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
# for f in 'zidane.jpg', 'bus.jpg':
#     torch.hub.download_url_to_file('https://ultralytics.com/images/' + f, f)  # download 2 images
# im1 = Image.open(os.path.join(repo_dir, 'data/images/zidane.jpg'))  # PIL image
# im2 = cv2.imread(os.path.join(repo_dir, 'data/images/bus.jpg'))[..., ::-1]  # OpenCV image (BGR to RGB)
im3 = Image.open(os.path.join(repo_dir, 'data/images/batch_1_000029.jpg'))  # PIL image

# Inference
# results = model(im1)  # batch of images
# results = model([im1, im2], size=640)  # batch of images
results = model([im3], size=640)  # batch of images

# Results
results.print()
results.save()
# results.show()
# results.save()  # or .show()

results.xyxy[0]  # im1 predictions (tensor)
results.pandas().xyxy[0]  # im1 predictions (pandas)
#      xmin    ymin    xmax   ymax  confidence  class    name
# 0  749.50   43.50  1148.0  704.5    0.874023      0  person
# 1  433.50  433.50   517.5  714.5    0.687988     27     tie
# 2  114.75  195.75  1095.0  708.0    0.624512      0  person
# 3  986.00  304.00  1028.0  420.0    0.286865     27     tie