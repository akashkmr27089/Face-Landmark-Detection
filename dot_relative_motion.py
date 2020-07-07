import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")
cap = cv2.VideoCapture(0)

while True:
	_, frame = cap.read()
	gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	for face in faces:
		x1 = face.left()
		y1 = face.top()
		x2 = face.right()
		y2 = face.bottom()
		x_avg = []
		y_avg = []
		
		landmarks = predictor(image = gray, box=face)
		for n in range(27,36):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			x_avg.append(x)
			y_avg.append(y)
			cv2.circle(img=frame, center=(x,y), radius=1, color=(0,255,0), thickness=-2)
		
		x_avg = sum(x_avg)/len(x_avg)
		y_avg = sum(y_avg)/len(y_avg) - 100
		cv2.circle(img=frame, center=(int(x_avg),int(y_avg)), radius=1, color=(0,0,255), thickness = 10)
		cv2.imshow(winname="Face", mat=frame)
		if cv2.waitKey(delay=1) == 27:
			break

cap.release()
cv2.destroyAllWindows()	
