# 80:20으로 나누기
import os
import random
import shutil
import json
import glob
from pathlib import Path
import shutil

targetDirName = "rotate"
fileList = glob.glob(targetDirName + "/*.txt")

print(type(fileList))
randomList = []
for file in fileList:
    imgName = Path(file).stem + ".jpg"
    imgPath = "data/rotate/" + imgName
    randomList.append(imgPath)

random.shuffle(randomList)
trainCount = int(len(randomList) * 0.8)
validCount = len(randomList) - trainCount

trainFile = open("rotate_train.txt", 'w', encoding='UTF-8')
validFile = open("rotate_valid.txt", 'w', encoding='UTF-8')
for i, file in enumerate(randomList):
    if i < trainCount:
        trainFile.write(file + "\n")
    else:
        validFile.write(file + "\n")

trainFile.close()
validFile.close()