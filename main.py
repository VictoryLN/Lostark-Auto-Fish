import numpy
import pyautogui
import imutils
import cv2
import time

# разрешение экрана
class screen:   
    weight = 1920
    height = 1080
flag = False

while(1)
    if flag == True:
        pyautogui.press('w')
        time.sleep(5)
    # создание скриншота
    image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # картиночки
    template = cv2.imread("template.png", 0)

    # поиск шаблона на скрине
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    if (abs(cv2.minMaxLoc(template_coordinates)[3][0] - cv2.minMaxLoc(template_coordinates)[3][1])<=10):
        print("Time to fish!")
        pyautogui.press('w')
        flag = True
        time.sleep(7)
    else:
        print("Not time yet!")
        flag = False