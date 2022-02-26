import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random

fishing_keybind = "3"

# разрешение экрана
class screen:   
    weight = 1920
    height = 1080
flag = "pulled"

# шаблоны
template = cv2.imread("template.png", 0)
poplavok = cv2.imread("poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "starting auto fish")
time.sleep(5)

while(1):
    if flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod [1]")
        pyautogui.keyDown(fishing_keybind)
        time.sleep( random.uniform( 0.05, 0.1 ))
        pyautogui.keyUp(fishing_keybind)
        flag = "thrown"
        time.sleep( random.uniform(4.5, 6.5))        
        

    # создание скриншота
    image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # поиск шаблона на скрине
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where( template_coordinates >= 0.7)


    # исходя из результатов поиска либо нажwимается W либо ничего не происходит и цикл идет по новой
    if len(loc[0]) > 0:
        if flag == "thrown":  
            print(strftime("%H:%M:%S", gmtime()), "Time to fish!")
            time.sleep(random.uniform(0.2, 1.0))
            pyautogui.keyDown(fishing_keybind)
            time.sleep( random.uniform( 0.05, 0.1 ))
            pyautogui.keyUp(fishing_keybind)
            flag = "pulled"
            time.sleep(random.uniform(8.5, 10.5))

    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing a fishing rod [2]")
        pyautogui.keyDown(fishing_keybind)
        time.sleep( random.uniform( 0.05, 0.1 ))
        pyautogui.keyUp(fishing_keybind)
        flag = "thrown"
        time.sleep( random.uniform(4.5, 6.5))

    print(strftime("%H:%M:%S", gmtime()), "Not time yet!")
    time.sleep(0.5)
            
            
    
