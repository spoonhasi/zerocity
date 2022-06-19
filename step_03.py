# 신호등과 신호 라벨만 골라서 Yolo용 라벨 제조하여 학습데이터 생성
import os
import shutil
import json
import glob
from pathlib import Path
import shutil

saveImagesDirName = "images"
saveLabelsJsonDirName = "labels_json"
lableJsonFileList = glob.glob(saveLabelsJsonDirName + "/*.json")

saveTrafficDirName = "traffic_datasets"
if os.path.isdir(saveTrafficDirName) == False:
    os.mkdir(saveTrafficDirName)

for i, file in enumerate(lableJsonFileList):
    print(i, file)
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    imageWidth = int(data['images']['width'])
    imageHeight = int(data['images']['height'])
    oneLabel = ""
    for item in data['annotations']:
        labelId = int(item['label_id'])
        # 신호등 44, 신호등_초록 45, 신호등_주황 46, 신호등_빨강 47, 신호등_방향표시 48
        # 신호등  0, 신호등_초록  1, 신호등_주황  2, 신호등_빨강  3, 신호등_방향표시  4
        if labelId >= 44 and labelId <= 48:
            info = item['info']
            positionX = (info[0] + (info[2]/2))/imageWidth
            positionY = (info[1] + (info[3]/2))/imageHeight
            width = info[2]/imageWidth
            height = info[3]/imageHeight
            oneLabel = oneLabel + str(labelId - 44) + " " + str(positionX) + " " + str(positionY) + " " + str(width) + " " + str(height) + "\n"
    if oneLabel != "":
        imgName = Path(file).stem + ".jpg"
        imgPath = os.path.join(saveImagesDirName, imgName)
        imgCopyPath = os.path.join(saveTrafficDirName, imgName)
        shutil.copy(imgPath, imgCopyPath)
        txtName = Path(file).stem + ".txt"
        with open(os.path.join(saveTrafficDirName, txtName), 'w', encoding="UTF-8") as annoFile:
            annoFile.write(oneLabel)
print("complete")