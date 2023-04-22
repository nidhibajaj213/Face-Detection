import cv2
face_cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img=cv2.imread("/Users/bajajnidhi/Downloads/IMG_0221.JPG",1)
'''gray_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05)
print(type(faces))
print(faces)
for x,y,w,h in faces:
    img=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)'''
resized=cv2.resize(img,(int(img.shape[1]/2),int(img.shape[0]/2)))
cv2.imshow("nid",resized)
cv2.waitKey(20000)
cv2.destroyAllWindows()
