import cv2

if __name__ == '__main__':
    rtsp = 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=2&subtype=0'
    cap = cv2.VideoCapture(rtsp)
    while True:
        ret, frame = cap.read()  # 获取一帧
        print(ret)
        if ret:
            cv2.imwrite('/chase/videoSave/test/1.jpg', frame)