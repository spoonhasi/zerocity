import glob
import json
import sys
import urllib.request as urllib
import os


saveImagesDirName = "images"
saveLabelsJsonDirName = "labels_json"

imgFileList = glob.glob(saveImagesDirName + "/*.jpg")

lableJsonFileList = glob.glob(saveLabelsJsonDirName + "/*.json")

saveDirName = "raw_datas"
fileList = glob.glob(saveDirName + "/*.json")

ListFileName = "check_01.txt"
f2 = open(ListFileName, "w")
for file in fileList:
    with open(file, 'r') as f:
        data = json.load(f)
    i = 0
    dataCount = len(data)
    print(dataCount)
    while True:
        f2.write(data[i]['image_flph'] + '\n')
        i = i + 1
        if i == dataCount:
            break
f2.close()
print("complete")