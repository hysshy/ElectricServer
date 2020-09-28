import cv2
import shutil
import os

if __name__ == '__main__':
    imgSrc = '/chase/videoSave'
    savePath = '/chase/dataset/0922/1-15/wrong'

    for cameraId in os.listdir(imgSrc):
        for data in os.listdir(imgSrc+'/'+cameraId):
            for wr in os.listdir(imgSrc+'/'+cameraId+'/'+data):
                if wr == 'right':
                    continue
                for id in os.listdir(imgSrc+'/'+cameraId+'/'+data+'/'+wr):
                    for imgName in os.listdir(imgSrc+'/'+cameraId+'/'+data+'/'+wr+'/'+id):
                        shutil.copy(imgSrc+'/'+cameraId+'/'+data+'/'+wr+'/'+id+'/'+imgName, savePath+'/'+cameraId+'_'+imgName)

