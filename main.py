# cspace.py
import cv2
import numpy as np

cap = cv2.VideoCapture('filmik.MP4')
fourcc = cv2.VideoWriter_fourcc(*'mpv4')
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))

size = (frame_width, frame_height)
out = cv2.VideoWriter('GreenBlueVideo.mp4', fourcc, 50.0, size, True)

while (1):

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([94, 80, 2])
    upper_blue = np.array([126, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    lower1 = np.array([0, 150, 50])
    upper1 = np.array([5, 255, 255])

    lower2 = np.array([170, 150, 50])
    upper2 = np.array([180, 255, 255])

    lower_mask = cv2.inRange(hsv, lower1, upper1)
    upper_mask = cv2.inRange(hsv, lower2, upper2)

    full_mask = lower_mask + upper_mask + mask

    result = cv2.bitwise_and(frame, frame, mask=full_mask)

    cv2.imshow('mask', full_mask)
    cv2.imshow('result', result)
    out.write(result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()
out.release()
print("Video saved successfully.")
cv2.destroyAllWindows()
