import shutil
import os
import math

if __name__ == '__main__':
    filePath = "/chase/dataset/0922/1-15/rigth_draw"
    startId = 0
    imgNameList = os.listdir(filePath)
    imgNameList.sort()
    for imgName in imgNameList:
        startId += 1
        savePath = filePath+"/"+str(math.ceil(startId/500))
        if not os.path.exists(savePath):
            os.makedirs(savePath)
        shutil.move(filePath+"/"+imgName, savePath)