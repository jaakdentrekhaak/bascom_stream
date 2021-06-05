import cv2
import os
import json

file_dir = os.path.dirname(os.path.realpath(__file__))
with open(f'{file_dir}/config.json') as config:
    data = json.load(config)
    url = data['bascom_url']

cap = cv2.VideoCapture(url)

while(cap.isOpened()):
    _, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(20) & 0xFF == ord('q'): # Exit program with by pressing 'q'
        break
cap.release()
cv2.destroyAllWindows()