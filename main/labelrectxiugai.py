import json
import os
import cv2
def getAllFile(picPath, key):
    picList = []
    for root, dirs, files in os.walk(picPath):
        for file in files:
            if key in file:
                picList.append(os.path.join(root,file))
    return picList

if __name__ == '__main__':
    jsonPath = "/chase/dataset/electricdata/jsons"
    xiugaiPath = "/chase/dataset/electricdata/rectxiugai"
    jsonSavePath = "/chase/dataset/electricdata/jsons2"
    for fileName in os.listdir(jsonPath):
        print(fileName)
        with open(jsonPath+"/"+fileName, 'rb') as f:
            data = f.read()
            data = json.loads(data.decode())
            shapes = data["shapes"]
            for i in range(len(shapes)):
                shape = shapes[i]
                points = shape["points"]
                label = shape["label"]
                rectName = fileName.replace(".json","_"+str(i)+".jpg")
                for xiugaiLabel in os.listdir(xiugaiPath):
                    if os.path.exists(xiugaiPath+"/"+xiugaiLabel+"/"+rectName):
                        data["shapes"][i]["label"] = xiugaiLabel
            with open(jsonSavePath + "/" + fileName, "w") as f:
                json.dump(data, f)







