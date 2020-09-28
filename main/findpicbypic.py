import os
import shutil

if __name__ == '__main__':
    imgSrcPath = "/chase/dataset/electricdata/images"
    wrongPath = "/chase/dataset/electricdata/imagesLunyi"
    savePath = "/chase/dataset/electricdata/imagesLunyi"
    jsonSrcPath = '/chase/dataset/electricdata/jsons2'

    for imgName in os.listdir(wrongPath):
        os.remove(jsonSrcPath + "/" + imgName.replace('.jpg', '.json'))
        # if imgName in os.listdir(imgSrcPath):
            # os.remove(imgSrcPath+"/"+imgName)
            # os.remove(jsonSrcPath + "/" + imgName.replace('.jpg', '.json'))
            # shutil.move(imgSrcPath+"/"+imgName, savePath)