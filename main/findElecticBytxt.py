import shutil
savePath = "/chase/videoSave/electric"
txtFile = "/chase/videoSave/4.txt"
f = open(txtFile,'r')
while True:
    line = f.readline()[:-1]
    print(line)
    if not line:
        break
    shutil.move(line, savePath)