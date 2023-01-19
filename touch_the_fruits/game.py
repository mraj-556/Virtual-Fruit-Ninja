import cv2
import random,datetime as dt
from cvzone.HandTrackingModule import HandDetector as hd

cap = cv2.VideoCapture(0)

hand_detector_model = hd(maxHands=1,detectionCon=0.8)

x,y = random.randint(80,580) , random.randint(80,335)
fruits_imgs = ['bananana.png','mango.png','pineapple.png','pple.png','range.png','strawberry.png','watermelon.png']
fruit = random.randint(0,6)
point=0

# intro

start = dt.datetime.now()
while True:
    img = cv2.imread("imgs\logo.jpg")
    # img = cv2.resize(img,(img.shape[1]*3,img.shape[0]*3))
    img = cv2.resize(img,(680,480))
    cv2.putText(img,"Do\'t Touch ",(80,230),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,255),2)
    cv2.putText(img,"The Fruits...! ",(220,285),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,255),2)
    cv2.imshow("Don\'t Touch The Fruits",img)
    cv2.moveWindow("Don\'t Touch The Fruits",380,150)
    cur_time = dt.datetime.now()
    diff = cur_time-start
    if cv2.waitKey(1):
        if diff.total_seconds()>=5:
            break    

start = dt.datetime.now()
remaining_time = 10
it=0
restart = 1
while True and restart:
    s,frame = cap.read()
    frame = cv2.flip(frame,1)
    org_frame = frame
    hand_found = hand_detector_model.findHands(frame,draw=False)
    if hand_found:
        fingers_up = hand_detector_model.fingersUp(hand_found[0])
        if fingers_up==[0,1,0,0,0]:
            fing_x = hand_found[0]["lmList"][8][0]
            fing_y = hand_found[0]["lmList"][8][1]
            if -30<fing_x-(x+25)<=30 and -30<fing_y-(y+25)<=30:
                point+=1
                x,y = random.randint(50,580) , random.randint(80,335)
                fruit = random.randint(0,6)
    img = cv2.imread(f"imgs\{fruits_imgs[fruit]}")
    img = cv2.resize(img,(50,50))
    frame[y:y+50,x:x+50] = img
    cv2.putText(frame,f"Time : {remaining_time} Seconds",(50,40),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,0,255),2,cv2.LINE_AA)
    cv2.putText(frame,f"point : {point}",(380,40),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,85,0),2,cv2.LINE_AA)
    # cv2.moveWindow("Don\'t Touch The Fruits",380,150)
    cv2.imshow("Don\'t Touch The Fruits",frame)
    cur_time = dt.datetime.now()
    diff = cur_time-start
    if cv2.waitKey(1)==ord('q') or cv2.waitKey(1)==ord('Q'):
        break
    elif cv2.waitKey(1):
        if diff.total_seconds()>(0.9+it) and diff.total_seconds()<=(1+it):
            remaining_time-=1
            it +=1
        if diff.total_seconds()>=10:
            
            while True:
                cv2.putText(org_frame,f"Score : {point}",(250,200),cv2.FONT_HERSHEY_SIMPLEX,1,(0,85,0),2)
                cv2.putText(org_frame,f"Press Q : Quit",(250,250),cv2.FONT_HERSHEY_SIMPLEX,1,(0,85,0),2)
                cv2.putText(org_frame,f"Press R : Restart",(250,300),cv2.FONT_HERSHEY_SIMPLEX,1,(0,85,0),2)
                cv2.imshow("Don\'t Touch The Fruits",org_frame)
                if cv2.waitKey(1)==ord('q') or cv2.waitKey(1)==ord('Q'):
                    restart = 0
                    break
                elif cv2.waitKey(1)==ord('r') or cv2.waitKey(1)==ord('R'):
                    point = 0
                    start = dt.datetime.now()
                    remaining_time = 10
                    it=0
                    break
