# Single Object Tracking (SOT) is a detection-free tracking also known as visual object tracking.
# Here the object of interest is determined in the first frame then the tracker is then tasked
# with locating that unique target in all other given frames.

import cv2
import sys

tracker = cv2.legacy.TrackerMIL_create()
# Read video
video = cv2.VideoCapture("../videos/input/1.mp4")

# Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()

# Read first frame.
ok, frame = video.read()
if not ok:
    print("Cannot read video file")
    sys.exit()

# Uncomment the line below to select a different bounding box
bbox = cv2.selectROI("Tracking", frame)

# Initialize tracker with first frame and bounding box
ok = tracker.init(frame, bbox)

output_file_path = "../videos/output/object_tracking_outputs/output_2.avi"
# Obtain frame size information using get() method
frame_width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
frame_size = (frame_width, frame_height)
frames_per_second = 20
four_cc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
out = cv2.VideoWriter(output_file_path, four_cc, frames_per_second, frame_size)
while True:
    # Start timer
    timer = cv2.getTickCount()
    # Read a new frame
    ok, frame = video.read()
    
    # Exit the loop
    if not ok:
        break
    # Update tracker
    ok, bbox = tracker.update(frame)
    # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer)

    # Draw bounding box
    if ok:
        # Tracking success
        p1 = (int(bbox[0]), int(bbox[1]))
        p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (255, 0, 0), 2, 1)
    else:
        # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    # Display tracker type on frame
    cv2.putText(frame, tracker_type + " Tracker", (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # Display FPS on frame
    cv2.putText(frame, "FPS : " + str(int(fps)), (100, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
    # Write the frame
    out.write(frame)
    # Press Q on keyboard to stop recording
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Everything done, release the video capture and video write objects
video.release()
out.release()
