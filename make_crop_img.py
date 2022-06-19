from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import numpy as np
import os
import random
import shutil
import json
import glob
from pathlib import Path
import shutil
import sys

saveTrafficWithLightDirName = "traffic_with_light"
if os.path.isdir(saveTrafficWithLightDirName) == False:
    os.mkdir(saveTrafficWithLightDirName)

saveTrafficDirName = "traffic_datasets"

targetFileList = glob.glob(saveTrafficDirName + "/*.txt")
for index, file in enumerate(targetFileList):
    #file = saveTrafficDirName + "/CIT-SDB-3062-ct_2d_00043560.jpg"
    fileNameWithoutExt = Path(file).stem
    imgName = fileNameWithoutExt + ".jpg"
    txtName = fileNameWithoutExt + ".txt"
    imgPath = os.path.join(saveTrafficDirName, imgName)
    txtPath = os.path.join(saveTrafficDirName, txtName)
    image = Image.open(imgPath)
    imgSize = image.size
    imgWidth = imgSize[0]
    imgHeight = imgSize[1]
    with open(txtPath, 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for jndex, line in enumerate(lines):
            if line.startswith("0"):
                line = line.replace('\n', '')
                lineSplitList = line.split(' ')
                left0 = (imgWidth * float(lineSplitList[1])) - (imgWidth * float(lineSplitList[3]) / 2)
                right0 = (imgWidth * float(lineSplitList[1])) + (imgWidth * float(lineSplitList[3]) / 2)
                top0 = (imgHeight * float(lineSplitList[2])) - (imgHeight * float(lineSplitList[4]) / 2)
                bottom0 = (imgHeight * float(lineSplitList[2])) + (imgHeight * float(lineSplitList[4]) / 2)
                width0 = right0 - left0
                height0 = bottom0 - top0
                existLight = False
                for line2 in lines:
                    if line2.startswith("1") or line2.startswith("2") or line2.startswith("3") or line2.startswith("4"):
                        line2 = line2.replace('\n', '')
                        line2SplitList = line2.split(' ')
                        centerX = (imgWidth * float(line2SplitList[1]))
                        centerY = (imgHeight * float(line2SplitList[2]))
                        if left0 < centerX and centerX < right0 and top0 < centerY and centerY < bottom0:
                            existLight = True
                            newCenterX = (centerX - left0) / width0
                            newCenterY = (centerY - top0) / height0
                            newObjectWidth = (imgWidth * float(line2SplitList[3])) / width0
                            newObjectHeight = (imgHeight * float(line2SplitList[4])) / height0
                            width3 = width0 * newObjectWidth
                            height3 = height0 * newObjectHeight
                            positionX3 = (newCenterX * width0) - (width3 / 2)
                            positionY3 = (newCenterY * height0) - (height3 / 2)
                            if positionY3 + height3 > height0:
                                height3 = height3 - (positionY3 + height3 - height0)
                            if positionY3 < 0:
                                height3 = height3 - positionY3
                                positionY3 = 0
                            if positionX3 + width3 > width0:
                                width3 = width3 - (positionX3 + width3 - height0)
                            if positionX3 < 0:
                                width3 = width3 - positionX3
                                positionX3 = 0
                            newCenterX = (positionX3 + (width3 / 2)) / width0
                            newCenterY = (positionY3 + (height3 / 2)) / height0
                            newObjectWidth = width3 / width0
                            newObjectHeight = height3 / height0
                            with open(os.path.join(saveTrafficWithLightDirName, fileNameWithoutExt + "-" + str(jndex + 1) + ".txt"), "a", encoding="UTF-8-sig") as f2:
                                f2.write(str(int(line2SplitList[0]) - 1) + " " + str(newCenterX) + " " + str(newCenterY) + " " + str(newObjectWidth) + " " + str(newObjectHeight) + "\n")
                        #draw = ImageDraw.Draw(croppedImage)
                        #draw.rectangle((positionX3, positionY3, positionX3 + width3,positionY3 + height3), outline=(255,255,0), width=3)
                        #croppedImage.show()
                        #croppedImage
                if existLight == True:
                    print(fileNameWithoutExt)
                    croppedImage = image.crop((left0, top0, right0, bottom0))
                    croppedImage.save(os.path.join(saveTrafficWithLightDirName, fileNameWithoutExt + "-" + str(jndex + 1) + ".jpg"))
print("complete")