import cv2
import numpy as np
import face_recognition

imgsubrata1=face_recognition.load_image_file('Face Recog Pro//ImageBasic//subrata1.jpg')
imgsubrata1=cv2.cvtColor(imgsubrata1,cv2.COLOR_BGR2RGB)
imgsubrata2=face_recognition.load_image_file('Face Recog Pro//ImageBasic//subrata2.jpg')
imgsubrata2=cv2.cvtColor(imgsubrata2,cv2.COLOR_BGR2RGB)

faceloc1=face_recognition.face_locations(imgsubrata1)[0]
encodsub1=face_recognition.face_encodings(imgsubrata1)[0]
#print(faceloc1)
cv2.rectangle(imgsubrata1,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(0,255,255),2)

faceloc2=face_recognition.face_locations(imgsubrata2)[0]
encodsub2=face_recognition.face_encodings(imgsubrata2)[0]
#print(faceloc2)
cv2.rectangle(imgsubrata2,(faceloc2[3],faceloc2[0]),(faceloc2[1],faceloc2[2]),(255,0,255),2)


cv2.imshow('Subrata',imgsubrata1)
cv2.imshow('Subrata2',imgsubrata2)
cv2.waitKey(0)
