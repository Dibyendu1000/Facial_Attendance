import cv2
import numpy as np
import face_recognition

imgTrain=face_recognition.load_image_file('Face Recog Pro//ImageBasic//subhra2.jpg')
imgTrain=cv2.cvtColor(imgTrain,cv2.COLOR_BGR2RGB)
imgTest=face_recognition.load_image_file('Face Recog Pro//ImageBasic//subhra1.jpg')
imgTest=cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

faceloc1=face_recognition.face_locations(imgTrain)[0]
encodeTrain=face_recognition.face_encodings(imgTrain)[0]
#print(faceloc1)
cv2.rectangle(imgTrain,(faceloc1[3],faceloc1[0]),(faceloc1[1],faceloc1[2]),(0,255,255),2)

faceloc2=face_recognition.face_locations(imgTest)[0]
encodeTest=face_recognition.face_encodings(imgTest)[0]
#print(faceloc2)
cv2.rectangle(imgTest,(faceloc2[3],faceloc2[0]),(faceloc2[1],faceloc2[2]),(255,0,255),2)

results=face_recognition.compare_faces([encodeTrain],encodeTest)
faceDis=face_recognition.face_distance([encodeTrain],encodeTest)
print(results,faceDis)
#print("sub1:",encodeTrain)
#print("sub2:",encodeTest)

cv2.imshow('Subrata',imgTrain)
cv2.imshow('Test',imgTest)
cv2.waitKey(0)
