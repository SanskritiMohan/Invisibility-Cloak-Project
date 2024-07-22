
import cv2 # for image processing
import numpy as np 
cap = cv2.VideoCapture(0)
background = cv2.imread('./image.jpg')

while cap.isOpened():
    #caturing the live frame
    ret, current_frame = cap.read()
    if ret:
        #converting from rgb to hsv color space
        hsv_frame = cv2.cvtColor(current_frame, cv2.COLOR_BGR2HSV)

        # Range for lower pink
        l_pink = np.array([160, 100, 100])
        u_pink = np.array([170, 255, 255])
        mask1 = cv2.inRange(hsv_frame, l_pink, u_pink)
        # Range for upper pink
        l_pink = np.array([170, 100, 100])
        u_pink = np.array([180, 255, 255])
        mask2 = cv2.inRange(hsv_frame, l_pink, u_pink)
        # Generating the final pink mask
        pink_mask = mask1 + mask2
        pink_mask = cv2.morphologyEx(pink_mask, cv2.MORPH_OPEN, np.ones((3,3), np.uint8), iterations=10)
        pink_mask = cv2.morphologyEx(pink_mask, cv2.MORPH_DILATE, np.ones((3,3), np.uint8), iterations=1)
        # Substituting the pink portion with the background image
        part1 = cv2.bitwise_and(background, background, mask=pink_mask)
        # Detecting things which are not pink
        pink_free = cv2.bitwise_not(pink_mask)
        
        # If the cloak is not present, show the current image
        part2 = cv2.bitwise_and(current_frame, current_frame, mask=pink_free)
        # Final output
        cv2.imshow("Invisibility Cloak", part1 + part2)
        if cv2.waitKey(5) == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()