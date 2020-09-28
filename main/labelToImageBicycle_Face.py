from module.mmdetection.mmhy import mmhy_detect
import os
import cv2
import numpy as np
import base64
import json

def getAllPic(picPath):
    picList = []
    for root, dirs, files in os.walk(picPath):
        for file in files:
            if "jpg" in file:
                picList.append(os.path.join(root,file))
    return picList



if __name__ == '__main__':
    picList = getAllPic("/chase/dataset/findimg")
    labelPath = "/chase/dataset/findjson"
    classes = ("face", "electric", "bicycle")
    mmhy_detect.init_model("0")
    for pic in picList:
        img = cv2.imread(pic)
        # print(pic)
        face_bboxes, face_labels, face_kp, vs_pred, bicycle_bboxes, bicycle_labels = mmhy_detect.detect(img)
        shapes = []
        for i in range(len(face_labels)):
            label = classes[face_labels[i]]
            xmin, ymin, xmax, ymax, score = face_bboxes[i]
            xmin = int(xmin)
            ymin = int(ymin)
            xmax = int(xmax)
            ymax = int(ymax)

            shapeItem = {}
            shapeItem.setdefault("line_color","")
            points = []
            points.append([xmin,ymin])
            points.append([xmax,ymin])
            points.append([xmax,ymax])
            points.append([xmin,ymax])

            shapeItem.setdefault("points",points)
            shapeItem.setdefault("fill_color")
            shapeItem.setdefault("label",label)
            shapes.append(shapeItem)

        for i in range(len(bicycle_labels)):
            label = classes[bicycle_labels[i]]
            xmin, ymin, xmax, ymax, score = bicycle_bboxes[i]
            xmin = int(xmin)
            ymin = int(ymin)
            xmax = int(xmax)
            ymax = int(ymax)

            shapeItem = {}
            shapeItem.setdefault("line_color","")
            points = []
            points.append([xmin,ymin])
            points.append([xmax,ymin])
            points.append([xmax,ymax])
            points.append([xmin,ymax])

            shapeItem.setdefault("points",points)
            shapeItem.setdefault("fill_color")
            shapeItem.setdefault("label",label)
            shapes.append(shapeItem)

        res = {}
        res.setdefault("shapes", shapes)
        if len(face_labels) > 0 or len(bicycle_labels)>0:
            with open(pic, "rb") as f:  # 转为二进制格式
                base64_data = base64.b64encode(f.read()).decode()  # 使用base64进行加密
                res.setdefault("imageData", base64_data)
            res.setdefault("imagePath", "")
            res.setdefault("fillColor", [255, 0, 0, 128])
            res.setdefault("lineColor", [0, 255, 0, 128])
            with open(labelPath + "/" + pic.split("/")[-1].replace(".jpg", ".json"), "w") as f:
                json.dump(res, f)
        else:
            print(pic)

