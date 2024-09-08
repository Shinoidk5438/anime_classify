#下载好的第一时间请根据中文进行目录修改
#Please correct the code following the Chinese
import cv2
from ultralytics import YOLO
import os
if __name__ == "__main__":

    model = YOLO("修改成你的模型目录/last.pt")
    filenames = os.listdir(r"修改成你的图片存放目录")
    for file in filenames:
        img = cv2.imread("修改成你的图片目录"+file)
        result = model(img)[0]
        names  = result.names
        top1_label = result.probs.top1
        top5_label = result.probs.top5
        top1_conf  = result.probs.top1conf
        top5_conf  = result.probs.top5conf
        top1_name  = names[top1_label]
        print(f"{file} is {top1_name}, label = {top1_label}, confidence = {top1_conf:.4f}")

print("Press 'Enter' 2 exit")
input()

    
