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
    jsonPath = "/chase/tstjsons"
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
                nppoints = np.array(points).astype(int)
                print(fileName, nppoints.tolist())
                # for point in points:
                #     xlist.append(point[0])
                #     ylist.append(point[1])
                #     xmin = int(min(xlist))
                #     ymin = int(min(ylist))
                #     xmax = int(max(xlist))
                #     ymax = int(max(ylist))
                #     if not os.path.exists(rectPath+"/"+label):
                #         os.makedirs(rectPath+"/"+label)
                #     rectName = fileName.replace(".json","_"+str(i)+".jpg")
                #     print(label)
                #     print(rectName)
                #     cv2.imwrite(rectPath+"/"+label+"/"+fileName.replace(".json","_"+str(i)+".jpg"), img[ymin:ymax,xmin:xmax])






