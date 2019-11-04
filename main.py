import numpy as np
import pyautogui
import imutils
import cv2

#разрешение экрана (customizable)
class screen:   
    weight = 1920
    height = 1080

#создание скриншот
image = pyautogui.screenshot(region=(screen.weight/3, screen.height/3, 300, 300))
image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("pic.png", image)

#запись скриншота
image = cv2.imread("pic.png")
cv2.imshow("pic.png", image)

cv2.waitKey(0)