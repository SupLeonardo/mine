import cv2

# Capture the frame from the camera
cap = cv2.VideoCapture(0)

# Read the frame
ret, frame = cap.read()

# Display the frame
cv2.imshow('frame', frame)

# Release the camera
cap.release()

# Close all windows
cv2.destroyAllWindows()