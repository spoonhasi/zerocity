#특정폴더안에서 txt파일의 내용이 없을 경우 동일한 이름의 jpg도 삭제하는 프로그램
from PIL import Image, ImageDraw
from pathlib import Path
import sys
import os
import glob

#YOLO용 그림 그리기
#saveTrafficDirName = "traffic_datasets"
targetDirPath = "rotate"
targetFileList = glob.glob(targetDirPath + "/*.txt")
count = 0
for index, file in enumerate(targetFileList):
    imgName = Path(file).stem + ".jpg"
    imgPath = os.path.join(targetDirPath, imgName)
    lableName = Path(file).stem + ".txt"
    lablePath = os.path.join(targetDirPath, lableName)
    boolRemove = False
    with open(lablePath, 'r', encoding='UTF-8') as f:
        line = f.readline()
        if line == "":
            boolRemove = True
    if boolRemove:
        os.remove(lablePath)
        os.remove(imgPath)
        print(imgPath)
        count = count + 1
print(count)