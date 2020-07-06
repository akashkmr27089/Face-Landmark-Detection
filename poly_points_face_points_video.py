import cv2
import numpy as np
import dlib

detector = dlib.get_frontal_face_detector()

predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

cap = cv2.VideoCapture(0)

while True:
	_, img = cap.read()
	gray = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY)
	faces = detector(gray)

	for face in faces:
		x1 = face.left()
		y1 = face.top()
		x2 = face.right()
		y2 = face.bottom()
		
		landmarks = predictor(image = gray, box=face)
		
		# Jaw Points 0-16
		doc = []
		for n in range(0,17):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		# Right Brow Points 17-21	
		doc = []	
		for n in range(17,22):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		#Left Brow Points 22-26	
		doc = []	
		for n in range(22,27):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		#Nose Points 27-35
		doc = []	
		for n in range(27,36):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		#Right Eye 36-41
		doc = []	
		for n in range(36,42):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		#Left Eye 42-47
		doc = []	
		for n in range(42,48):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))
		
		#Mouth Points 48-60
		doc = []	
		for n in range(48,61):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))

		#Lips Points 61-67
		doc = []	
		for n in range(61,68):
			x = landmarks.part(n).x
			y = landmarks.part(n).y
			doc.append([x,y])
		pts = np.array(doc).astype(np.int32)
		pts = pts.reshape((-1,1,2))
		cv2.polylines(img, [pts], False, (0,255,255))
		
		cv2.imshow(winname="Face", mat=img)
		if cv2.waitKey(delay=1) == 27:
			break

cap.release()
cv2.destroyAllWindows()
