import cv2
import time
import threading
lock = threading.Lock()
from scene import Log
classes = ["electric", "bicycle"]
import os
from scene.capsdk import CapSdkServer

class SDKScene:
    def __init__(self, cameraId, cameraIp, port, admin, passwd, chn, elctric_model, scenename, points):
        self.cameraId = cameraId
        self.cameraIp = cameraIp
        self.port = port
        self.admin = admin
        self.passwd = passwd
        self.chn = chn
        self.elctric_model = elctric_model
        self.name = scenename
        self.points = points
        self.image = None
        self.flag = 1
        self.closeflag = 1
        self.savePath = "/chase/videoSave/"+str(cameraId)
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)
        self.cameraPath = '/chase/cameraSave/'+str(cameraId)
        if not os.path.exists(self.cameraPath):
            os.makedirs(self.cameraPath)
        self.sockAddress = '/chase/cameraSave/'+str(cameraId)+".sock"
        self.lastNum = 0
        self.maxNum = 3
        self.imgList = []
        self.id = 0


    def start(self):

        cap = CapSdkServer(self.cameraPath, self.sockAddress, self.cameraId,
                           self.cameraIp, self.port, self.admin, self.passwd, self.chn)
        cap.startCap()
        time.sleep(1)
        cap.sendmsg('2')
        while(True):
            time.sleep(1)
            self.image = cap.getSDKImg()
            if self.image is not None:
                ori_im = self.image.copy()
                # imgName = str(time.time())+str(".jpg")
                try:
                    start = time.time()
                    bicycle_bboxes, bicycle_labels = self.elctric_model.detect(ori_im, self.points)
                    end = time.time()
                    print(str(self.cameraId)+':'+"time: {}s, fps: {}".format(end - start, 1 / (end - start)))
                    # #保存原图
                    # cv2.imwrite(self.savePath + "/" + imgName, ori_im)
                    # #保存绘图
                    # for i in range(face_labels.size(0)):
                    #     label = face_labels[i].item()
                    #     labelName = classes[label]
                    #     bbox = face_bboxes[i].cpu().numpy().astype(int)
                    #     cv2.rectangle(ori_im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 1)
                    #     cv2.putText(ori_im, str(labelName), (bbox[0], bbox[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    #                 2)
                    #     kpitem = face_kp[i].cpu().numpy().astype(int)
                    #     for i in range(5):
                    #         point = (kpitem[i * 2], kpitem[i * 2 + 1])
                    #         cv2.circle(ori_im, point, 3, (255, 0, 0), 0)
                    #
                    # for i in range(bicycle_bboxes.size(0)):
                    #     label = bicycle_labels[i].item()
                    #     labelName = classes[label]
                    #     bbox = bicycle_bboxes[i].cpu().numpy().astype(int)
                    #     cv2.rectangle(ori_im, (bbox[0], bbox[1]), (bbox[2], bbox[3]), (0, 255, 0), 1)
                    #     cv2.putText(ori_im, str(labelName), (bbox[0], bbox[1]), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    #                 2)
                    # cv2.imwrite(self.drawPath + "/" + imgName, ori_im)
                    #记录检测到电动车的图片
                    if len(bicycle_labels) > 0:
                        self.lastNum += 1
                        # self.imgList.append(ori_im)
                        cv2.imwrite(self.savePath + "/" + str(time.time())+'.jpg', ori_im)
                    # else:
                    #     if self.lastNum >= self.maxNum:
                    #         data = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                    #         if not os.path.exists(self.savePath+'/'+data+'/right/'+str(self.id)):
                    #             os.makedirs(self.savePath+'/'+data+'/right/'+str(self.id))
                    #         for i in range(len(self.imgList)):
                    #             img = self.imgList[i]
                    #             imgName = data+'_'+str(self.id)+'_'+str(i)+'.jpg'
                    #             cv2.imwrite(self.savePath+'/'+data+'/right/'+str(self.id) + "/" + imgName, img)
                    #         self.id += 1
                    #         self.imgList.clear()
                    #         self.lastNum = 0
                    #
                    #     elif self.lastNum > 0:
                    #         data = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                    #         if not os.path.exists(self.savePath+'/'+data+'/wrong/'+str(self.id)):
                    #             os.makedirs(self.savePath+'/'+data+'/wrong/'+str(self.id))
                    #         for i in range(len(self.imgList)):
                    #             img = self.imgList[i]
                    #             imgName = data+'_'+str(self.id)+'_'+str(i)+'.jpg'
                    #             cv2.imwrite(self.savePath+'/'+data+'/wrong/'+str(self.id) + "/" + imgName, img)
                    #         self.id += 1
                    #         self.imgList.clear()
                    #         self.lastNum = 0

                except Exception as e:
                    Log.logger.exception(e)
                    Log.logger.error(str(self.cameraId)+'模型错误')
                    break
            else:
                time.sleep(1)
        Log.logger.warning(str(self.cameraId)+'场景关闭，图片释放')
