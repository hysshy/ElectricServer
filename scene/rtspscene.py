import cv2
import time
import datetime
import threading
lock = threading.Lock()
from scene import Log
classes = ["electric", "bicycle"]
import os

class RtspScene:
    def __init__(self, cameraId, rtsp, elctric_model, scenename, points):
        self.rtspid = cameraId
        self.rtsp = rtsp
        self.elctric_model = elctric_model
        self.name = scenename
        self.cap = cv2.VideoCapture(rtsp)
        self.points = points
        self.image = None
        self.flag = 1
        self.closeflag = 1
        self.savePath = "/chase/videoSave/"+str(cameraId)
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)
        self.lastNum = 0
        self.maxNum = 3
        self.imgList = []
        self.id = 0


    def start(self):

        t = threading.Thread(target=self.readFrame)
        t.setDaemon(True)
        t.start()
        while(True):
            time.sleep(1)
            if self.image is not None:
                ori_im = self.image.copy()
                # imgName = str(time.time())+str(".jpg")
                try:
                    start = time.time()
                    bicycle_bboxes, bicycle_labels = self.elctric_model.detect(ori_im, self.points)
                    end = time.time()
                    print(str(self.rtspid)+':'+"time: {}s, fps: {}".format(end - start, 1 / (end - start)))
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
                        self.imgList.append(ori_im)
                        # cv2.imwrite(self.savePath + "/" + str(time.time())+'.jpg', ori_im)
                    else:
                        if self.lastNum >= self.maxNum:
                            data = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                            if not os.path.exists(self.savePath+'/'+data+'/right/'+str(self.id)):
                                os.makedirs(self.savePath+'/'+data+'/right/'+str(self.id))
                            for i in range(len(self.imgList)):
                                img = self.imgList[i]
                                imgName = data+'_'+str(self.id)+'_'+str(i)+'.jpg'
                                cv2.imwrite(self.savePath+'/'+data+'/right/'+str(self.id) + "/" + imgName, img)
                            self.id += 1
                            self.imgList.clear()
                            self.lastNum = 0

                        elif self.lastNum > 0:
                            data = str(datetime.datetime.now().strftime('%Y-%m-%d'))
                            if not os.path.exists(self.savePath+'/'+data+'/wrong/'+str(self.id)):
                                os.makedirs(self.savePath+'/'+data+'/wrong/'+str(self.id))
                            for i in range(len(self.imgList)):
                                img = self.imgList[i]
                                imgName = data+'_'+str(self.id)+'_'+str(i)+'.jpg'
                                cv2.imwrite(self.savePath+'/'+data+'/wrong/'+str(self.id) + "/" + imgName, img)
                            self.id += 1
                            self.imgList.clear()
                            self.lastNum = 0

                except Exception as e:
                    Log.logger.exception(e)
                    Log.logger.error(str(self.rtspid)+'模型错误')
                    break
        Log.logger.warning(str(self.rtspid)+'场景关闭，图片释放')


    # thread: read frame
    def readFrame(self):
        f = 0
        time.sleep(2)
        Log.logger.info('startrtsp')
        while (True):
            try:
                ret, frame = self.cap.read()  # 获取一帧
                if ret:
                    self.image = frame
                    f = 0
                else:
                    Log.logger.warning(str(self.rtspid) + '无法获取画面')
                    self.cap.release()
                    self.image = None
                    if f < 10:
                        time.sleep(15)
                        self.cap = cv2.VideoCapture(self.rtsp)
                        Log.logger.warning('尝试重联')
                        f += 1
                    else:
                        break
            except Exception as e:
                Log.logger.exception(e)
        self.cap.release()
        Log.logger.warning('cap.release()')
