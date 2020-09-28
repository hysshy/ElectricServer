from module.mmdetection.mmhy import mmhy_detect
from scene.rtspscene import RtspScene
from scene.sdkscene import SDKScene
import threading
import time

def startRtspScene(cameraId, rtsp, model, sceneName, points):
    sceneItem = RtspScene(cameraId,rtsp,model,sceneName, points)
    sceneItem.start()

def startSdkScene(cameraId, cameraIp, port, admin, passwd, chn, model, sceneName, points):
    sceneItem = SDKScene(cameraId, cameraIp, port, admin, passwd, chn, model, sceneName, points)
    sceneItem.start()

if __name__ == '__main__':
    mmhy_detect.init_model(0)

    # rtspList = [['1','rtsp://admin:admin123@10.10.51.133/cam/realmonitor?channel=1&subtype=0','rtsp']]
    rtspList = [
                # ['1', 'rtsp', 'rtsp://admin:1111@192.168.18.147:554', [[440,400],[940,140],[1500,800],[940,1080]]],
                # ['2', 'rtsp', 'rtsp://admin:1111@192.168.18.148:554','rtsp',[[860,460],[1200,400],[1440,1080],[960,1080]]],
                # #['3', 'rtsp', 'rtsp://admin:1111@192.168.18.149:554','rtsp'], #无法获取
                # ['4', 'rtsp', 'rtsp://admin:1111@192.168.18.150:554','rtsp',[[460,500],[920,480],[1200,1080],[600,1080]]],
                # # ['5', 'rtsp', 'rtsp://admin:1111@192.168.18.155:554','rtsp'],
                # #['6', 'rtsp', 'rtsp://admin:1111@192.168.18.156:554','rtsp'],#无法获取
                # #['7', 'rtsp', 'rtsp://admin:1111@192.168.18.157:554','rtsp'],#无法获取
                # #['8', 'rtsp', 'rtsp://admin:1111@192.168.18.158:554','rtsp'],#无法获取
                # # ['9','rtsp', 'rtsp://admin:1111@192.168.18.159:554','rtsp'],
                # ['10', 'rtsp', 'rtsp://admin:86976655jk@192.168.20.2:554/h264/ch1/main/av_stream', [[460,250], [1110,100], [1450,760], [800,1060]]],
                # ['11', 'rtsp', 'rtsp://admin:86976655jk@192.168.20.64:554/h264/ch1/main/av_stream',[[160, 600], [650, 500], [1520, 1080], [600, 1080]]],
                # ['12', 'rtsp', 'rtsp://admin:86976655jk@192.168.20.68:554/h264/ch1/main/av_stream',[[444, 200], [1000, 100], [1400, 822], [800, 1080]]],
                # ['13', 'rtsp', 'rtsp://admin:xxh123@10.200.202.184:554/cam/realmonitor?channel=1&subtype=0',[[230, 125], [458,118], [465,574], [238,575]]],
                # ['14', 'rtsp', 'rtsp://admin:admin111111@192.168.16.8:554/cam/realmonitor?channel=2&subtype=0',[[100, 300], [260, 136], [500, 500], [464, 575], [235, 575]]],
                ['15', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '1', [[520,480],[980,460],[1180,1080], [720,1080]]],
                # ['16', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '2', [[694, 375], [1020, 347], [1310, 1079], [725, 1076]]],
                # ['17', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '3', [[1260, 470], [1598, 291], [1920, 727], [1913, 1071], [1439, 1077]]],
                ['18', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '4', [[1232, 422], [1663, 245], [1915, 842], [1903, 1077], [1436, 1080]]],
                ['19', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '5', [[549, 410], [859, 295], [1384, 1075], [731, 1077]]],
                # ['20', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '6', None],
                # ['21', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '7', [[487, 505], [825, 413], [1178, 1074], [598, 1079]]],
                ['22', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '8', [[520, 570], [884, 475], [1196, 1075], [774, 1080], [615, 1076]]],
                ['23', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '9', [[816, 321], [1134, 342], [1110, 1080], [622, 1080]]],
                # ['24', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '10', [[1115, 760], [1523, 636], [1739, 1079], [1168, 1076]]],
                # ['25', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '11', None],
                # ['26', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '12', [[792, 476], [1139, 369], [1602, 1072], [947, 1077]]],
                ['27', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '13', [[1110, 769], [1437, 670], [1623, 1074], [1164, 1076]]],
                ['28', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '14', [[439, 409], [763, 327], [1189, 1075], [559, 1080]]],
                ['29', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '15', [[789, 475], [1120, 374], [1602, 1076], [954, 1077]]],
                # ['30', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '16', None],
        ['31', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '17', [[764, 376], [1039, 194], [1822, 932], [1663, 1080], [1146, 1077], [773, 398]]],
        ['32', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '18', [[561, 627], [888, 553], [1161, 1077], [656, 1079]]],
        # ['33', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '19', None],
        # ['34', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '20', None],
        ['35', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '21', [[728, 318], [1118, 312], [1147, 1076], [665, 1077]]],
        # ['36', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '22', None],
        # ['37', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '23', None],
        # ['38', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '24', None],
        # ['39', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '25', None],
        ['40', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '26', [[427, 352], [792, 175], [1475, 1003], [1408, 1077], [753, 1077]]],
        ['41', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '27', [[388, 461], [745, 334], [1272, 1077], [556, 1079]]],
        ['42', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '28', [[678, 390], [1082, 381], [1196, 1074], [623, 1075]]],
        # ['43', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '29', None],
        # ['44', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '30', [[759, 348], [1221, 310], [1335, 1077], [734, 1072]]],
        # ['45', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '31', None],
        # ['46', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '32', None],
        # ['47', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '33', None],
        # ['48', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '34', None],
        ['49', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '35', [[561, 479], [892, 352], [1397, 1079], [1011, 1080], [747, 1077]]],
        # ['50', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '36', None],
        # ['51', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '37', None],
        ['52', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '38', [[496, 545], [798, 457], [1260, 1077], [635, 1079]]],
        ['53', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '39', [[558, 114], [973, 7], [1406, 826], [1003, 1072], [783, 1076], [525, 428]]],
        ['54', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '40', [[879, 574], [1153, 499], [1460, 1076], [999, 1074]]],
        ['55', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '41', [[631, 380], [1084, 190], [1625, 1042], [888, 1079], [630, 412]]],
        ['56', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '42', [[780, 226], [1239, 81], [1708, 919], [1408, 1077], [1116, 1074]]],
        ['57', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '43', [[736, 662], [1185, 475], [1573, 1077], [878, 1077]]],
        # ['58', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '44', None],
        # ['59', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '45', None],
        # ['60', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '46', None],
        ['61', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '47', [[566, 588], [931, 404], [1506, 1074], [770, 1076]]],
        # ['62', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '48', None],
        # ['63', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '49', None],
        # ['64', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '50', None],
        ['65', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '51', [[803, 689], [1304, 583], [1464, 1080], [860, 1079]]],
        # ['66', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '52', None],
        # ['67', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '53', None],
        # ['68', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '54', None],
        ['69', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '55', [[637, 294], [1077, 102], [1563, 821], [1168, 1080], [1017, 1072]]],
        # ['70', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '56', None],
        # ['71', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '57', None],
        ['72', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '58', [[731, 676], [1244, 657], [1259, 1075], [713, 1079]]],
        # ['73', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '59', None],
        # ['74', 'dhsdk', '192.168.25.109', '37777', 'admin', 'admin123', '60', None],
                # ['27', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=17&subtype=0', 'rtsp', None],
                # ['28', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=18&subtype=0', 'rtsp', None],
                # ['29', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=19&subtype=0', 'rtsp', None],
                # ['30', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=22&subtype=0', 'rtsp', None],
        #         ['31', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=25&subtype=0', 'rtsp', None],
        #         ['32', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=27&subtype=0', 'rtsp', None],
        #         ['33', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=28&subtype=0', 'rtsp', None],
        #         ['34', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=29&subtype=0', 'rtsp', None],
        #         ['35', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=30&subtype=0', 'rtsp', None],
        #         ['36', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=31&subtype=0', 'rtsp', None],
        #         ['37', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=35&subtype=0', 'rtsp', None],
        #         ['38', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=36&subtype=0', 'rtsp', None],
        #         ['39', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=39&subtype=0', 'rtsp', None],
        #         ['39', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=39&subtype=0', 'rtsp', None],
        #         ['39', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=39&subtype=0', 'rtsp', None],
        # ['40', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=40&subtype=0', 'rtsp', None],
        # ['41', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=41&subtype=0', 'rtsp', None],
        # ['42', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=42&subtype=0', 'rtsp', None],
        # ['43', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=43&subtype=0', 'rtsp', None],
        # ['44', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=44&subtype=0', 'rtsp', None],
        # ['45', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=46&subtype=0', 'rtsp', None],
        # ['46', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=48&subtype=0', 'rtsp', None],
        # ['47', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=50&subtype=0', 'rtsp', None],
        # ['48', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=52&subtype=0', 'rtsp', None],
        # ['49', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=53&subtype=0', 'rtsp', None],
        # ['50', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=55&subtype=0', 'rtsp', None],
        # ['51', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=56&subtype=0', 'rtsp', None],
        # ['52', 'rtsp://admin:admin123@192.168.25.109:554/cam/realmonitor?channel=59&subtype=0', 'rtsp', None],

    ]

    for rtspItem in rtspList:
        if rtspItem[1] == 'dhsdk':
            t = threading.Thread(target=startSdkScene, args=(rtspItem[0],rtspItem[2],rtspItem[3],rtspItem[4],rtspItem[5],rtspItem[6],mmhy_detect,rtspItem[1],rtspItem[7]))
            t.start()
        if rtspItem[1] == 'rtsp':
            t = threading.Thread(target=startRtspScene, args=(rtspItem[0],rtspItem[2],mmhy_detect,rtspItem[1],rtspItem[3]))
            t.start()
        time.sleep(5)
    t.join()

