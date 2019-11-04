import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime

# разрешение экрана
class screen:   
    weight = 1920
    height = 1080
flag = False

# шаблон
template = cv2.imread("template.png", 0)

while(1):
    if flag == True:
        pyautogui.press('w')
        time.sleep(5)

    # создание скриншота
    image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # поиск шаблона на скрине
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)

    # исходя из результатов поиска либо нажимается W либо ничего не происходит и цикл идет по новой
    if (abs(cv2.minMaxLoc(template_coordinates)[3][0] - cv2.minMaxLoc(template_coordinates)[3][1])<=5):
        print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
        pyautogui.press('w')
        flag = True
        time.sleep(7)
    else:
        print(strftime("%H:%M:%S", gmtime()),"Not time yet!")
        flag = False