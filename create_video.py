import cv2, os
import numpy as np

save_folder = "JPEGImages"
dir = os.chdir(save_folder)
files = os.listdir(dir)

# height,width,layers=files[0].shape

img=[]
for file in files:
    img.append(cv2.imread(file))

height,width,layers=img[1].shape

# choose codec according to format needed
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
video = cv2.VideoWriter('video.avi', fourcc, 1, (width, height))

for _ in range(10):
    for file in files:
        img = cv2.imread(file)
        video.write(img)

cv2.destroyAllWindows()
video.release()