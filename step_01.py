#제로시티 데이터 다운로드

import requests
import json
import os

saveDirName = "raw_datas" #데이터를 저장할 폴더
if os.path.isdir(saveDirName) == False:
    os.mkdir(saveDirName)

apiKey = 'Encoding인증키' #Decoding
apiKeyDecode = requests.utils.unquote(apiKey)
totalCount = 0
url = 'http://apis.data.go.kr/C100006/zerocity/getCctvList/event/2DBoundingBox'

for eventTypeNumber in range(1, 8): #1부터 7까지 7개 타입의 이벤트를 받기 위함
    eventTypeStr = str(eventTypeNumber).zfill(2)
    pageNo = 1
    tmpTotalJsonData = []
    while True:
        params ={'serviceKey' : apiKeyDecode, 'type' : 'json', 'numOfRows' : 1000, 'pageNo' : pageNo, 'eventType' : eventTypeStr, 'startDt' : '2019-01-01', 'endDt' : '2022-12-31' }
        result = requests.get(url, params=params).json()
        if result[0]['resultCode'] == "0":
            tmpTotalJsonData = tmpTotalJsonData + result[0]['cctvfileList']
            print("event_type_" + eventTypeStr + " page_number : " + str(pageNo))

        else:
            print("event_type_" + eventTypeStr + " done, count : " + str(len(tmpTotalJsonData)))
            break
        pageNo = pageNo + 1
    with open(saveDirName + "/event_type_" + eventTypeStr + '.json', 'w') as outfile:
        json.dump(tmpTotalJsonData, outfile, indent=4)
    totalCount = totalCount + len(tmpTotalJsonData)
print("complete, total_count : " + str(totalCount))