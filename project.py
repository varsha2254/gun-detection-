import cv2
import numpy as np
import imutils

# Load cascade file
gun_cascade = cv2.CascadeClassifier("cascade.xml")

if gun_cascade.empty():
    print("Error: cascade.xml file not found!")
    exit()

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Cannot access camera!")
    exit()

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to capture frame")
        break

    frame = imutils.resize(frame, width=500)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    guns = gun_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5,
        minSize=(100, 100)
    )

    if len(guns) > 0:
        print("Gun Detected")

    for (x, y, w, h) in guns:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("Security Feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()