import torch


def load_model(repo_dir, model_load_path, source='local', device='cpu'):
    if source != 'local':
        model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)  # force_reload = recache latest code
        return model
    model = torch.hub.load(repo_dir, 'custom', path=model_load_path, source=source, device=device)
    model.eval()
    return model
