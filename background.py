import cv2 #for image processing
#creating a videocapture object
cap = cv2.VideoCapture(0) #webcam
#getting background image
while cap.isOpened():
    ret, background = cap.read() #simply reading from the webcam
    if ret:
        cv2.imshow("image", background)
        if cv2.waitKey(5) == ord('q'):
            #save the background image
            cv2.imwrite("image.jpg", background)
            break
cap.release()
cv2.destroyAllWindows()