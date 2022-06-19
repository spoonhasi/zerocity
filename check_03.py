import glob
import json
import sys
import urllib.request as urllib
import os


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
    if cctvNumber not in cctvList:
        cctvList.append(cctvNumber)

f2 = open(ListFileName, "w", encoding="UTF-8-sig")
cctvList.sort()

tmpDictionaty = {}
for i in cctvList:
    tmpDictionaty[i] = 0

for i, file in enumerate(lableJsonFileList):
    print(i, file)
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    cctvNumber = data['images']['cctv_type'] + "-" + data['images']['cctv_id']
    tmpDictionaty[cctvNumber] = tmpDictionaty[cctvNumber] + 1

for i in cctvList:
    f2.write(i + "-count_" + str(tmpDictionaty[i]).zfill(4) + '\n')
f2.close()
print("complete")