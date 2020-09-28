import json
import os
import cv2
import numpy as np
def getAllFile(picPath, key):
    picList = []
    for root, dirs, files in os.walk(picPath):
        for file in files:
            if key in file:
                picList.append(os.path.join(root,file))
    return picList

if __name__ == '__main__':
    labelPath = "/chase/dataset/jsons/electric"
    imagePath = "/chase/dataset/images/electric"
    jsonFile = "/chase/dataset/electric.json"

    imgList = getAllFile(imagePath, ".jpg")

    jsonFileLists = os.listdir(labelPath)
    annotations = []
    categories = []
    images = []
    info = {"year":0}
    licenses = [{"id":1,"name":"","url":""}]
    type = "instances"
    categoriesName = ["electric", "bicycle", 'background']
    # categoriesName = ["face"]
    id = 1
    image_id = 0
    nokey = 0
    for cate_i in range(len(categoriesName)):
        categories.append({"id":cate_i+1, "name":categoriesName[cate_i], "supercategory":categoriesName[cate_i]})
    for imgFile in imgList:
        print(imgFile)
        jsonName = imgFile.split("/")[-1].split(".jpg")[0]+".json"
        if jsonName not in jsonFileLists:
            print(imgFile + "找不到json文件")
        else:
            with open(labelPath+"/"+jsonName, 'rb') as f:
                img = cv2.imread(imgFile)
                imgName = imgFile.split("/")[-2]+"/"+imgFile.split("/")[-1]

                data = f.read()
                data = json.loads(data.decode())
                facebboxs = []
                facelabels = []
                faceLandmarks = []
                visibles = []
                facesegs = []
                shapes = data["shapes"]

                image_id += 1
                images.append(
                    {"date_captured": "", "file_name": imgName, "height": img.shape[0], "width": img.shape[1],
                     "license": 1, "url": "", "id": image_id})
                for i in range(len(shapes)):
                    shape = shapes[i]
                    points = shape["points"]
                    label = shape["label"]
                    if label not in categoriesName:
                        continue
                    category_id = categoriesName.index(label) + 1
                    xlist = []
                    ylist = []
                    for point in points:
                        xlist.append(point[0])
                        ylist.append(point[1])
                    xmin = int(min(xlist))
                    ymin = int(min(ylist))
                    xmax = int(max(xlist))
                    ymax = int(max(ylist))
                    items = {"area": (xmax - xmin) * (ymax - ymin),
                                 "bbox": [xmin, ymin, xmax - xmin, ymax - ymin],
                                 "segmentation": [[xmin,ymin, xmax,ymin, xmax,ymax, xmin,ymax]],
                                 "id": id, "image_id": image_id, "iscrowd": 0, "category_id": category_id}
                    id += 1
                    annotations.append(items)

    res = {"info":info, "licenses":licenses, "type":type,
           "categories":categories, "images":images, "annotations":annotations}
    print(len(annotations))
    with open(jsonFile, "w") as f:
        json.dump(res, f)








