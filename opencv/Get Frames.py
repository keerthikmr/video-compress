import cv2
import os

video = cv2.VideoCapture('C:\\Users\\Admin\\Downloads\\Video\\Sports_360P-1d5c.mkv')

frame_number = 0 

while True:
    ret, frame = video.read()

    if not ret:
        break

    frame_filename = os.path.join('Frames', f'frame_{frame_number}.jpg')
    cv2.imwrite(frame_filename, frame)

    frame_number += 1
