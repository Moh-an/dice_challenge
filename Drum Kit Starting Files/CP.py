import cv2
import sys

window_name='Camera Preview'
s=0

if len(sys.argv)>1:
    s=sys.argv[1]

source=cv2.VideoCapture(0)

while cv2.waitKey(1)!=27:
    has_frame, camera_frame=source.read()
    if not has_frame:
        break
    cv2.imshow(window_name,camera_frame)
source.release()
cv2.destroyWindow(window_name)