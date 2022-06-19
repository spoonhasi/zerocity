import glob
import json
import sys
import urllib.request as urllib
import os
from pathlib import Path


saveImagesDirName = "images"
saveLabelsJsonDirName = "labels_json"
saveDirName = "raw_datas"

imgFileList = glob.glob(saveImagesDirName + "/*.jpg")

lableJsonFileList = glob.glob(saveLabelsJsonDirName + "/*.json")

fileList = glob.glob(saveDirName + "/*.json")

cctvIdList = []
ListFileName = "check_03.txt"

cctvList = []
for i, file in enumerate(lableJsonFileList):
    print(i, file)
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    cctvNumber = data['images']['cctv_type'] + "-" + data['images']['cctv_id']
    jsonOldName = Path(file).stem + ".json"
    imgOldName = Path(file).stem + ".jpg"
    jsonNewName = cctvNumber + "-" + Path(file).stem + ".json"
    imgNewName = cctvNumber + "-" + Path(file).stem + ".jpg"
    jsonOldName = os.path.join(saveLabelsJsonDirName, jsonOldName)
    imgOldName = os.path.join(saveImagesDirName, imgOldName)
    jsonNewName = os.path.join(saveLabelsJsonDirName, jsonNewName)
    imgNewName = os.path.join(saveImagesDirName, imgNewName)
    print(jsonOldName)
    print(imgOldName)
    print(jsonNewName)
    print(imgNewName)
    os.rename(jsonOldName, jsonNewName)
    os.rename(imgOldName, imgNewName)
print("complete")