import cv2
import re
import os
import time

# URL = "http://localhost:5000/video_feed"
# video = cv2.VideoCapture(URL)

video = cv2.VideoCapture('video.avi')

"""
save_folder = "JPEGImages"
dir = os.chdir(save_folder)
files = os.listdir(dir)
cnt = 0
# print(os.getcwd())
for file in files:
    # print(file)
    index = re.search('.jpg', file)
    if index:
        cnt = cnt + 1
"""

while True:
    ret, img = video.read()
    # if not img.any() == None:
    cv2.imshow("Stream Video",img)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break