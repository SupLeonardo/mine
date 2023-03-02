import cv2
vid = cv2.VideoCapture(0)
while(True):
    ret, frame = vid.read()
    frame = frame[100: int(frame.shape[0]-200), 200:int(frame.shape[1]-300)]
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()