# 위치기반신호추정

from PIL import Image, ImageDraw


testImageFilePath = "predict_traffic_light_by_position.jpg"
testLabelFilePath = "predict_traffic_light_by_position.txt"

with open(testLabelFilePath, 'r', encoding='UTF-8') as f:
    lines = f.readlines()
    positionList = lines[0].split(' ')
    objectCenterXposiotionRatio = float(positionList[1])
    objectCenterYposiotionRatio = float(positionList[2])
    objectWidthRatio = float(positionList[3])
    objectHeightRatio = float(positionList[4])

img = Image.open(testImageFilePath)
imgSize = img.size
imgWidth = imgSize[0]
imgHeight = imgSize[1]
print(str(imgWidth) + " / " + str(imgHeight))
ratio = imgWidth / imgHeight
trafficLightType = 0
print("가로/세로 비율 : " + str(ratio))
if 3 < ratio: #차량신호등 4구
    if objectCenterXposiotionRatio < 0.25:
        print("빨간신호")
    elif objectCenterXposiotionRatio < 0.5:
        print("노란신호")
    elif objectCenterXposiotionRatio < 0.75:
        print("좌회전신호")
    else:
        print("초록신호")
elif 1 < ratio: #차량신호등 3구
    if objectCenterXposiotionRatio < 0.33:
        print("빨간신호")
    elif objectCenterXposiotionRatio < 0.66:
        print("노란신호")
    else:
        print("초록신호")
else: #보행신호등 2구
    if objectCenterYposiotionRatio < 0.5:
        print("빨간신호")
    else:
        print("초록신호")
