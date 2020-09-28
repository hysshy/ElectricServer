from mmdet.apis import init_detector, inference_detector
import threading
lockDetect = threading.Lock()


config_file = '/chase/hyelectric_mmdetection/tools/work_dirs/0921/ms_rcnn_regnet3.2_fpn_1x_coco/ms_rcnn_regnet3.2_fpn_1x_coco.py'
checkpoint_file = '/chase/hyelectric_mmdetection/tools/work_dirs/0921/ms_rcnn_regnet3.2_fpn_1x_coco/epoch_18.pth'

def init_model(gpuId):
    global mmhy_model
    mmhy_model = init_detector(config_file, checkpoint_file, device='cuda:'+str(gpuId))

def detect(img, points=None):
    result = inference_detector(mmhy_model, img, points, lockDetect)
    return result

if __name__ == '__main__':
    init_model(0)
    detect("/media/chase/Elements/2020行人属性数据集/images/i11850.jpg",None)




