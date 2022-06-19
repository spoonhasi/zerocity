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
ListFileName = "check_02.txt"
f2 = open(ListFileName, "w", encoding="UTF-8-sig")
for i, file in enumerate(lableJsonFileList):
    #print(i, file)
    with open(file, 'r', encoding='UTF-8') as f:
        data = json.load(f)
    infoSumList = []
    delList = []
    for index, item in enumerate(data['annotations']):
        infoSum = str(item['info'][0]) + "," + str(item['info'][1]) + "," + str(item['info'][2]) + "," + str(item['info'][3])
        if infoSum in infoSumList:
            f2.write(file + " : " + item['annotation_id'] + ', ' + item['label_name'] + '\n')
            delList.append(index)
        else:
            infoSumList.append(infoSum)
    if len(delList) != 0:
        delList.reverse()
        print(i, file)
        for index in delList:
            print(index)
            del(data['annotations'][index])
    with open(file, 'w', encoding='UTF-8') as f:
        json.dump(data, f, indent='\t', ensure_ascii=False)
f2.close()
print("complete")