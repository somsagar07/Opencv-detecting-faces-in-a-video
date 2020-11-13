import cv2

# Load the cascade
face_cascade = cv2.CascadeClassifier('xml\haarcascade_frontalface_default.xml')
#use video file path(file.mp4) as input 
video = cv2.VideoCapture('file.mp4')

while True:
    # Read the frame
    _,frame = video.read()
    # Convert to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # Detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 3)
    # Draw the rectangle around each face
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('frame', frame)
    # Stop if esca pe key is pressed
    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the VideoCapture object
video.release()

