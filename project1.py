#comments added

import cv2
import numpy as np
import urllib
face_data="haarcascade_frontalface_default.xml"
classifier=cv2.CascadeClassifier(face_data)
URL='http://10.20.246.217:8080/shot.jpg'
data=[]
ret=True
while ret:
    image_url=urllib.request.urlopen(URL)
    image=np.array(bytearray(image_url.read()),np.uint8)
    frame=cv2.imdecode(image,-1)
    faces=classifier.detectMultiScale(frame)
    if faces is not None:
        for x,y,w,h in faces:
            face_image=frame[y:y+h,x:x+w].copy()
            if len(data)<=150:
                data.append(face_image)
            else:
                cv2.putText(frame,'complete',(250,250),
                cv2.FONT_HERSHEY_PLAIN,1,(255,0,0),2)
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)
        cv2.imshow('capturing',frame)
        
        if  cv2.waitKey(1)==27:
            break;
cv2.destroyAllWindows()

name = input('Enter the name')

c=0
for i in data:
    cv2.imwrite('images/'+name+'_'+str(c)+'.jpg',i)
    c+=1
