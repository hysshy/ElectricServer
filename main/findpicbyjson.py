import os
import shutil

if __name__ == '__main__':
    imgPath = '/chase/dataset/0825/backgroundImgaes'
    jsonPath = '/chase/dataset/0825/backgroundjsons'
    savePath = '/chase/dataset/0825/no'
    for imgName in os.listdir(imgPath):
        jsonName = imgName.replace('.jpg','.json')
        if not jsonName in os.listdir(jsonPath):
            shutil.move(imgPath+'/'+imgName, savePath)