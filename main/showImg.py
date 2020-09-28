import cv2

if __name__ == '__main__':
    img = cv2.imread('/media/chase/My Passport/chase/videoSave/15/1600247419.9248939.jpg')
    img = cv2.resize(img, (int(img.shape[1]/2), int(img.shape[0]/2)))
    cv2.imshow('test', img)
    cv2.waitKey()