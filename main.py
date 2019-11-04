import numpy
import pyautogui
import imutils
import cv2

# разрешение экрана (customizable)
class screen:   
    weight = 1920
    height = 1080

# создание скриншота
image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
image = cv2.cvtColor(numpy.array(image), cv2.COLOR_RGB2BGR)
cv2.imwrite("screenshot.png", image)

# запись скриншота
image = cv2.imread('screenshot.png', 0)
#cv2.imshow("screenshot", image)

# шаблон
template = cv2.imread("template.png", 0)
#cv2.imshow("template", template)

# поиск шаблона на скрине
template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
if (abs(cv2.minMaxLoc(template_coordinates)[3][0] - cv2.minMaxLoc(template_coordinates)[3][1])<=20):
    print("Time to fish")
else:
    print("not time yet")
