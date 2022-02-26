import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import sys

fishing_keybind = "3"

if len(sys.argv) > 1:
    energy = int(sys.argv[1])
else:
    energy = 10000

# init
class screen:   
    (weight, height) = pyautogui.size() 
flag = "pulled"

# load template images
template = cv2.imread("template.png", 0)
poplavok = cv2.imread("poplavok.png", 0)

print(strftime("%H:%M:%S", gmtime()), "starting auto fish, switch to lost ark window within 5 seconds")
time.sleep(5)

failed = 0
while energy > 0 and failed < 3:
    if flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing fishing rod. Starting energy: ", energy)
        pyautogui.keyDown(fishing_keybind)
        time.sleep(max(0.05,random.gauss(0.12, 0.05)))
        pyautogui.keyUp(fishing_keybind)
        flag = "thrown"
        start_time = time.time()
        compare_count = 0
        failed = 0
        time.sleep( random.uniform(4.5, 6.5))        

    # take screenshot
    image = pyautogui.screenshot(region=(screen.weight/2 - 100, screen.height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # openCV try to match template
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where( template_coordinates >= 0.7)


    # exclamation point matched
    if len(loc[0]) > 0:
        if flag == "thrown":  
            print(strftime("%H:%M:%S", gmtime()), "CATCH!")
            time.sleep(max(0.15,random.gauss(0.3, 0.1)))
            pyautogui.keyDown(fishing_keybind)
            time.sleep(max(0.05,random.gauss(0.12, 0.05)))
            pyautogui.keyUp(fishing_keybind)
            flag = "pulled"
            energy -= 60
            time.sleep(random.uniform(8.5, 10.5))

    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        print(strftime("%H:%M:%S", gmtime()), "throwing fishing rod. Energy remaining: ", energy)
        pyautogui.keyDown(fishing_keybind)
        time.sleep(max(0.05,random.gauss(0.12, 0.05)))
        pyautogui.keyUp(fishing_keybind)
        flag = "thrown"
        start_time = time.time()
        compare_count = 0
        failed = 0
        time.sleep(random.uniform(4.5, 6.5))

    compare_count += 1
    if not (compare_count % 50):
        print("waiting for fish...")

    if time.time() - start_time > 15:
        failed += 1
        print("FAILED")
        pyautogui.keyDown(fishing_keybind)
        time.sleep(max(0.05,random.gauss(0.12, 0.05)))
        pyautogui.keyUp(fishing_keybind)
        flag = "pulled"
        sleep(5)
        continue
            
print("out of energy, exiting") 
    
