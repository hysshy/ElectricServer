import os
import shutil

if __name__ == '__main__':
    filePath = "/chase/videoSave/1"
    for path in os.listdir(filePath):
        for img in os.listdir(filePath+"/"+path):
            shutil.move(filePath+"/"+path+"/"+img, filePath)