import threading
import socket
import cv2
import time
import os


class CapSdkServer:
    def __init__(self, saveFile, sockAddress, id, ip, port=37777, admin="admin", passwd="admin123", chn=0):
        self.saveFile = saveFile
        self.camera_id = id
        self.ip = ip
        self.port = port
        self.admin = admin
        self.passwd = passwd
        self.chn = chn
        self.sockAddress = sockAddress
        self.lock = threading.Lock()
        self.logout_status = 1
        self.f = 0
        self.out = 0
        self.out3 = 0

    def clearImg(self):
        time.sleep(0.0000001)
        print(str(self.ip)+":clean")
        with self.lock:
            if os.path.exists(self.saveFile):
                for img in os.listdir(self.saveFile):
                    os.remove(self.saveFile + "/" + img)

    def osrun(self):
        print('保存路径：'+str(self.saveFile)+',设备ip:'+str(self.ip)+',端口:'+str(self.port)+',用户名:'+str(self.admin)
              +',密码：'+str(self.passwd)+',通讯文件：'+str(self.sockAddress))
        os.system("java -jar /home/chase/sdk/netsdk.jar"
                  +" "+self.saveFile+" "+self.ip+" "+str(self.port)
                  +" "+self.admin+" "+self.passwd+" "+self.sockAddress+" "+str(self.chn))

    def start_clean(self):
        while self.logout_status == 1:
            #print('清空图片目录')
            # time.sleep(300)
            time.sleep(300)
            self.clearImg()
        print(str(self.ip)+'退出清理'+str(self.logout_status))
        with self.lock:
            if os.path.exists(self.saveFile):
                os.rmdir(self.saveFile)
                os.remove(self.sockAddress)


    def startCap(self):
        t = threading.Thread(target=self.osrun)
        t.start()
        time.sleep(3)
        t2 = threading.Thread(target=self.start_clean)
        t2.start()

    def sendmsg(self, msg):
        # tcp协议对应为SOCK_STREAM
        self.client_sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)

        # connect方法用来连接服务器
        self.client_sock.connect(self.sockAddress)
        # send()方法想服务器发送数据
        self.client_sock.send(msg.encode())


        # recv()接收对方发送过来的数据，最大接收1024个字节
        recv_data = self.client_sock.recv(1024).decode()
        self.client_sock.close()
        #print("收到了服务器的回应信息：%s" % recv_data)
        return recv_data


    def getSDKImg(self):
        time.sleep(0.0000001)
        with self.lock:
            #try:
            imgFile = self.sendmsg("0")
            #print(imgFile)
            time.sleep(0.05)
            img = None
            if imgFile != 'null':
                img = cv2.imread(imgFile)

            else:
                print(str(self.camera_id)+':设备链接异常' + str(self.f))
                print(self.ip)
                print('登出')
                self.logout_self()
                self.out = 1
                print('设备链接异常，断开链接')
                self.restart()
                #self.f += 1
            return img
            #except Exception as ex:
            #    logger.exception(ex)
            #    globalv.status[self.camera_id] = 0
            #    #self.logout()
            #    self.logout_status = 0
            #    return None

    def logout_self(self):
        self.sendmsg("1")

    def logout(self):
        self.logout_status = 0
        self.sendmsg("3")
        self.out3 = 1

    def restart(self):
        while self.out == 1:
            time.sleep(10)
            if self.out3 == 0:
                print("重新启动")
                loginstatus = self.sendmsg("2")
                if loginstatus == "success":
                    self.out = 0
                print('loginstatus:'+str(loginstatus))

if __name__ == '__main__':
    # cap = CapSDK_Server("/home/chase/DHSDK/Capture/2","10.10.51.127", 37777,"admin",
    #                     "admin123","/home/chase/test.sock")
    # cap.startCap()
    cap = CapSdkServer("/home/chase/DHSDK/Capture" + str(5), "/home/chase/DHSDK/Capture" + str(5) + ".sock", 1,  "192.168.25.109", "37777", "admin", "admin123", 1)
    cap.startCap()
    time.sleep(2)
    cap.sendmsg('2')
    # cap.getSDKImg()

    # while True:
    #     time.sleep(1)
