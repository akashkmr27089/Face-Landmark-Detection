import cv2
import dlib
# Load the detector
detector = dlib.get_frontal_face_detector()
# read the image
img = cv2.imread("./face.png")
# Convert image into grayscale

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
# Use detector to find landmarks
faces = detector(gray)
for face in faces:
    x1 = face.left() # left point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    # Draw a rectangle
    #cv2.rectangle(img=img, pt1=(x1, y1), pt2=(x2, y2), color=(0, 255, 0), thickness=4)
    landmarks = predictor(image=gray, box=face)
    for n in range(0,68):
	    x = landmarks.part(n).x
	    y = landmarks.part(n).y
# show the image
cv2.imshow(winname="Face", mat=img)
# Wait for a key press to exit
cv2.waitKey(delay=0)
# Close all windows
cv2.destroyAllWindows()	
