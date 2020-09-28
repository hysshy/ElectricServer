import os
import shutil

if __name__ == '__main__':
    imgSrcPath = "/chase/dataset/electricdata/images"
    jsonSrcPath = '/chase/dataset/electricdata/jsons'
    rectPath = "/chase/dataset/electricdata/rectxiugai/mohuelectric"
    imgsavePath = "/chase/dataset/electricdata/mohuImages"
    jsonSavePath = '/chase/dataset/electricdata/mohuJsons'

    for rect in os.listdir(rectPath):
        print(rect)
        imgName = rect.split("_")[0]+".jpg"
        if os.path.exists(imgSrcPath+"/"+imgName):
            shutil.move(imgSrcPath+"/"+imgName, imgsavePath)
            shutil.move(jsonSrcPath+'/'+imgName.replace('.jpg', '.json'), jsonSavePath)