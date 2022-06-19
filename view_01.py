#bbox 그리기
from PIL import Image, ImageDraw
from pathlib import Path
import sys
import os
import glob

#YOLO용 그림 그리기
#saveTrafficDirName = "traffic_datasets"
saveTrafficWithLightBboxDirName = "traffic_only_datasets_bbox"
if os.path.isdir(saveTrafficWithLightBboxDirName) == False:
    os.mkdir(saveTrafficWithLightBboxDirName)

saveTrafficWithLightDirName = "traffic_only_datasets"
targetFileList = glob.glob(saveTrafficWithLightDirName + "/*.txt")
for index, file in enumerate(targetFileList):
    dataName = Path(file).stem
    resizeRate = 1

    imgName = Path(dataName).stem + ".jpg"
    imgPath = os.path.join(saveTrafficWithLightDirName, imgName)
    lableName = Path(dataName).stem + ".txt"
    lablePath = os.path.join(saveTrafficWithLightDirName, lableName)
    print(imgPath)

    img = Image.open(imgPath)
    imgSize = img.size
    imgWidth = imgSize[0]
    imgHeight = imgSize[1]

    imgResized = img.resize((int(imgWidth * resizeRate),int(imgHeight * resizeRate)))
    imgResizedSize = imgResized.size
    imgResizedWidth = imgResizedSize[0]
    imgResizedHeight = imgResizedSize[1]

    draw = ImageDraw.Draw(imgResized)

    with open(lablePath, 'r', encoding='UTF-8') as f:
        while True:
            line = f.readline()
            line = line.replace('\n', '')
            positionlist = line.split(' ')
            if len(positionlist) > 1:
                width = imgResizedWidth * float(positionlist[3])
                height = imgResizedHeight * float(positionlist[4])
                positionX = (float(positionlist[1]) * imgResizedWidth) - (width / 2)
                positionY = (float(positionlist[2]) * imgResizedHeight) - (height / 2)
                if positionlist[0] == "0":
                    draw.rectangle((positionX, positionY, positionX + width,positionY + height), outline=(255,255,0), width=3)
                else:
                    draw.rectangle((positionX, positionY, positionX + width,positionY + height), outline=(0,255,0), width=3)
            if not line:
                break
    imgResized.save(os.path.join(saveTrafficWithLightBboxDirName, imgName))
#imgResized.show()