from app import app
from extensions import db
from database_models import WeightsModel


def init_COCO_weights():
    with app.app_context():
        COCO_yolov5n = WeightsModel(weights_name='COCO_yolov5n',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5n.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5s = WeightsModel(weights_name='COCO_yolov5s',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5s.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5m = WeightsModel(weights_name='COCO_yolov5m',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5m.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5l = WeightsModel(weights_name='COCO_yolov5l',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5l.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5x = WeightsModel(weights_name='COCO_yolov5x',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5x.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5n6 = WeightsModel(weights_name='COCO_yolov5n6',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5n6.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5s6 = WeightsModel(weights_name='COCO_yolov5s6',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5s6.pt',
                               weights_version='yolov5-7.0',
                               enable=True,
                               dataset_id=1)
        COCO_yolov5m6 = WeightsModel(weights_name='COCO_yolov5m6',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5m6.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5l6 = WeightsModel(weights_name='COCO_yolov5l6',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5l6.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        COCO_yolov5x6 = WeightsModel(weights_name='COCO_yolov5x6',
                               weights_relative_path='weights/yolov5-7.0/COCO_yolov5x6.pt',
                               weights_version='yolov5-7.0',
                               dataset_id=1)
        db.session.add_all([COCO_yolov5n,
                            COCO_yolov5s,
                            COCO_yolov5m,
                            COCO_yolov5l,
                            COCO_yolov5x,
                            COCO_yolov5n6,
                            COCO_yolov5s6,
                            COCO_yolov5m6,
                            COCO_yolov5l6,
                            COCO_yolov5x6])
        db.session.commit()


def init_Sample_weights():
    with app.app_context():
        Sample_yolov5n_300_epochs = WeightsModel(weights_name='Sample_yolov5n_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5n_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5s_300_epochs = WeightsModel(weights_name='Sample_yolov5s_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5s_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5l_300_epochs = WeightsModel(weights_name='Sample_yolov5l_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5l_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5m_300_epochs = WeightsModel(weights_name='Sample_yolov5m_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5m_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5x_300_epochs = WeightsModel(weights_name='Sample_yolov5x_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5x_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5n6_300_epochs = WeightsModel(weights_name='Sample_yolov5n6_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5n6_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5s6_300_epochs = WeightsModel(weights_name='Sample_yolov5s6_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5s6_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               enable=True,
                               dataset_id=2)
        Sample_yolov5l6_300_epochs = WeightsModel(weights_name='Sample_yolov5l6_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5l6_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5m6_300_epochs = WeightsModel(weights_name='Sample_yolov5m6_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5m6_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        Sample_yolov5x6_300_epochs = WeightsModel(weights_name='Sample_yolov5x6_300_epochs',
                               weights_relative_path='weights/yolov5-6.2/Sample_yolov5x6_300_epochs.pt',
                               weights_version='yolov5-6.2',
                               dataset_id=2)
        db.session.add_all([Sample_yolov5n_300_epochs,
                            Sample_yolov5s_300_epochs,
                            Sample_yolov5m_300_epochs,
                            Sample_yolov5l_300_epochs,
                            Sample_yolov5x_300_epochs,
                            Sample_yolov5n6_300_epochs,
                            Sample_yolov5s6_300_epochs,
                            Sample_yolov5m6_300_epochs,
                            Sample_yolov5l6_300_epochs,
                            Sample_yolov5x6_300_epochs])
        db.session.commit()

def init_TACO_weights():
    with app.app_context():
        TACO_yolov5s_300_epochs = WeightsModel(weights_name='TACO_yolov5s_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/TACO_yolov5s_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               enable=True,
                               dataset_id=3)
        TACO_yolov5l_300_epochs = WeightsModel(weights_name='TACO_yolov5l_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/TACO_yolov5l_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=3)
        TACO_yolov5m_300_epochs = WeightsModel(weights_name='TACO_yolov5m_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/TACO_yolov5m_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=3)
        TACO_yolov5x_300_epochs = WeightsModel(weights_name='TACO_yolov5x_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/TACO_yolov5x_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=3)
        db.session.add_all([TACO_yolov5s_300_epochs,
                            TACO_yolov5m_300_epochs,
                            TACO_yolov5l_300_epochs,
                            TACO_yolov5x_300_epochs])
        db.session.commit()

def init_Garbage_weights():
    with app.app_context():
        Garbage_yolov5s_300_epochs = WeightsModel(weights_name='Garbage_yolov5s_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/Garbage_yolov5s_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               enable=True,
                               dataset_id=4)
        Garbage_yolov5l_300_epochs = WeightsModel(weights_name='Garbage_yolov5l_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/Garbage_yolov5s_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=4)
        Garbage_yolov5m_300_epochs = WeightsModel(weights_name='Garbage_yolov5m_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/Garbage_yolov5s_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=4)
        Garbage_yolov5x_300_epochs = WeightsModel(weights_name='Garbage_yolov5x_300_epochs',
                               weights_relative_path='weights/yolov5-3.1/Garbage_yolov5s_300_epochs.pt',
                               weights_version='yolov5-3.1',
                               dataset_id=4)
        db.session.add_all([Garbage_yolov5s_300_epochs,
                            Garbage_yolov5m_300_epochs,
                            Garbage_yolov5l_300_epochs,
                            Garbage_yolov5x_300_epochs])
        db.session.commit()


if __name__ == '__main__':
    init_COCO_weights()
    init_Sample_weights()
    init_TACO_weights()
    init_Garbage_weights()
