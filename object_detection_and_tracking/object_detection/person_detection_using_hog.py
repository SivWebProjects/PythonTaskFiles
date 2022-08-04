# Import the necessary packages
import numpy as np
import cv2

# Initialize the HOG descriptor/person detector
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Open video stream
cap = cv2.VideoCapture("../videos/input/1.mp4")
out = cv2.VideoWriter("../videos/hod_output.avi", cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 15, (640, 480))
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Exit the loop
    if not ret:
      break
      
    # resizing for faster detection
    frame = cv2.resize(frame, (640, 480))
    # detect people in the frame
    # returns the bounding boxes for the detected objects
    boxes, weightebcam s = hog.detectMultiScale(frame, winStride=(8, 8), scale=1.02)
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])

    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB), (0, 255, 0), 2)

    # Write the output video
    out.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the video capture and video write objects
cap.release()
out.release()
# Close all the frames
cv2.destroyAllWindows
