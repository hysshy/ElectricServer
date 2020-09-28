import os
import shutil

if __name__ == '__main__':
    imgSrcPath = "/chase/dataset/electricdata/images"
    rectPath = "/chase/dataset/electricdata/rect2/lunyi"
    savePath = "/chase/dataset/electricdata/imagesLunyi"

    for rect in os.listdir(rectPath):
        print(rect)
        imgName = rect.split("_")[0]+".jpg"
        shutil.copy(imgSrcPath+"/"+imgName, savePath)