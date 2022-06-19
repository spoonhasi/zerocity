#데이터에서 url추출하여 image와 annotation파일 다운로드

import glob
import json
import sys
import urllib.request as urllib
import os

saveDirName = "raw_datas" #데이터포탈에서 받은 json파일이 있는 폴더
if os.path.isdir(saveDirName) == False:
    sys.exit("no raw_datas")

saveImagesDirName = "images" #이미지를 저장할 폴더
if os.path.isdir(saveImagesDirName) == False:
    os.mkdir(saveImagesDirName)

saveLabelsJsonDirName = "labels_json" #annotation파일(json)을 저장할 폴더
if os.path.isdir(saveLabelsJsonDirName) == False:
    os.mkdir(saveLabelsJsonDirName)

fileList = glob.glob(saveDirName + "/*.json")

for file in fileList:
    with open(file, 'r') as f:
        data = json.load(f)
    i = 0
    dataCount = len(data)
    while True:
        try:
            urllib.urlretrieve(data[i]['image_flph'], "./" + saveImagesDirName + "/" + data[i]['image_file'])
            urllib.urlretrieve(data[i]['cctv_json_stor_flph'], "./" + saveLabelsJsonDirName + "/" + data[i]['cctv_json_file'])
            i = i + 1
            print(file + " : " + str(i) + "/" + str(dataCount))
        except Exception as e:
            print("download error, retry")
        if i == dataCount:
            break

print("complete")