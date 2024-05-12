# importing cv2 library which is used for image processing and detection
import cv2


face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml") #import dataset from cv2 to detect face muscles
video_capture = cv2.VideoCapture(0) #open camera
while True:
    ret , video_data = video_capture.read()  #read from open camera
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY) #convert to black and white
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30),
        flags=cv2.CASCADE_SCALE_IMAGE
    )                                           
    for(x,y,w,h) in faces:
        cv2.rectangle(video_data,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.imshow("Smit Cam",video_data) # used to open the window with name and data is displayed
    if cv2.waitKey(10) == ord("a"): # if a is pressed then window will close
        break
video_capture.release()  # after capturing release the data

