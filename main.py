import cv2
import winsound     
cam=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi',fourcc, 20.0, (640,480))
while cam.isOpened():
    ret,frame1 = cam.read()
    ret, frame2 = cam.read()
    diff=cv2.absdiff(frame1,frame2)
    cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    gray=cv2.cvtColor(diff,cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    _,thresh=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)
    dilated=cv2.dilate(thresh,None,iterations=3)
    contours,_= cv2.findContours(dilated,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    if ret==True:
        out.write(frame1)
##    cv2.drawContours(frame1,contours,-1,(0,0,255),2)
    for c in contours:
        if cv2.contourArea(c)<2000:
            continue
        x,y,w,h=cv2.boundingRect(c)
        
        winsound.PlaySound('alt.wav',winsound.SND_ASYNC)
        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)
    if cv2.waitKey(5)==ord('q'):
        break
    cv2.imshow("Granny Cam",frame1)

cam.release()
out.release()
cv2.destroyAllWindows()
