import numpy
import pyautogui
import cv2
import time
from time import gmtime, strftime
import random
import yaml
from PIL import Image

# screen resolution
screen_width, screen_height= pyautogui.size()

# Keybindings
with open("resources/keybindings.yaml", "r") as yamlfile:
    keybindings = yaml.safe_load(yamlfile)



# Variables
flag = "pulled"
counter = 1
idletimer = 0
fishing_task_state = "Accepted"

# template images
# if needed, create your own template images
template = cv2.imread(f"resources/{screen_height}/template.png", 0)
poplavok = cv2.imread(f"resources/{screen_height}/poplavok.png", 0)
acceptTask = cv2.imread(f"resources/{screen_height}/acceptTask.png", 0)
submitTask = cv2.imread(f"resources/{screen_height}/submitTask.png", 0)
perfect_zone = Image.open(f"resources/{screen_height}/perfectZone.png")
moving_arrow = Image.open(f"resources/{screen_height}/movingArrow.png")
cool_feeling = Image.open(f"resources/{screen_height}/5.png")
esc_btn = Image.open(f"resources/{screen_height}/esc.png")
cool_feeling_region = (1047, 1278, 18, 21)
game_bar_region = (670, 240, 15, 560)
esc_btn_region = (19,139,130,40)
arrow_region_xOffset, arrow_region_width, arrow_region_height = 21, 40, 560


print(f"screenHeight:{screen_height}, screenWidth:{screen_width}")
print(strftime("%H:%M:%S", gmtime()), "Starting the bot in 5 seconds. Automatic repair every 50 casts.")
time.sleep(5)

def moveCursorToLake(screen_width, screen_height):
    # Move cursor to lake
    print(strftime("%H:%M:%S", gmtime()), "Moving cursor to lake.")
    xOffset = 0.273
    yOffset = 0.687
    moveToX3 = round(screen_width * xOffset)
    moveToY3 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX3, y=moveToY3, clicks=0, button='left')


# Function to cast fishing rod ingame
def castFishingRod(count):
    print(strftime("%H:%M:%S", gmtime()), f"Casting fishing rod. Counter: {count}")

    # Cast fishing rod ingame
    pyautogui.keyDown(keybindings['fishing'])
    time.sleep( random.uniform( 0.25, 0.55 ))
    pyautogui.keyUp(keybindings['fishing'])
    time.sleep( random.uniform(4.5, 6.5))

# Function with all steps to repair the fishing rod through the pet inventory
def repairFishingRod(screen_width, screen_height):
    if keybindings['pet-inventory-modifier'] != None and keybindings['pet-inventory-modifier'] != '':
        print(strftime("%H:%M:%S", gmtime()), f"Opening pet inventory ({keybindings['pet-inventory-modifier'].upper()} + {keybindings['pet-inventory']}).")
        # Open pet inventory
        pyautogui.keyDown(keybindings['pet-inventory-modifier'])
        pyautogui.keyDown(keybindings['pet-inventory'])
        pyautogui.keyUp(keybindings['pet-inventory'])
        pyautogui.keyUp(keybindings['pet-inventory-modifier'])
    else:
        print(strftime("%H:%M:%S", gmtime()), f"Opening pet inventory ({keybindings['pet-inventory']}).")
        # Open pet inventory
        pyautogui.keyDown(keybindings['pet-inventory'])
        pyautogui.keyUp(keybindings['pet-inventory'])

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Small repair button offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on Pet Function: remote repair.")
    xOffset = 0.625
    yOffset = 0.641
    moveToX1 = round(screen_width * xOffset)
    moveToY1 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair LifeTool offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on Repair All button.")
    xOffset = 0.625
    yOffset = 0.859
    moveToX2 = round(screen_width * xOffset)
    moveToY2 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=1, button='left')

    # Repair All offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on Repair All button.")
    xOffset = 0.391
    yOffset = 0.718
    moveToX2 = round(screen_width * xOffset)
    moveToY2 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair OK offset
    print(strftime("%H:%M:%S", gmtime()), "Clicking on OK button.")
    xOffset = 0.457
    yOffset = 0.578
    moveToX3 = round(screen_width * xOffset)
    moveToY3 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX3, y=moveToY3, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX3, y=moveToY3, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(4.0, 5.0))

    # Press ESC
    print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing repair window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Press ESC
    print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing pet window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')



def acceptGuildFishingTask(screen_width, screen_height):
    global fishing_task_state
    if keybindings['unas-task'] is not None and keybindings['unas-task-modifier'] != '':
        print(strftime("%H:%M:%S", gmtime()), f"Opening Una's task ({keybindings['unas-task-modifier'].upper()} + {keybindings['unas-task']}).")
        # Open Una's task
        pyautogui.keyDown(keybindings['unas-task-modifier'])
        pyautogui.keyDown(keybindings['unas-task'])
        pyautogui.keyUp(keybindings['unas-task'])
        pyautogui.keyUp(keybindings['unas-task-modifier'])
    else:
        print(strftime("%H:%M:%S", gmtime()), f"Opening Una's task ({keybindings['unas-task']}).")
        # Open pet inventory
        pyautogui.keyDown(keybindings['unas-task'])
        pyautogui.keyUp(keybindings['unas-task'])

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    print(strftime("%H:%M:%S", gmtime()), "Clicking on Guild Task.")
    # Guild Task tab button offset
    xOffset = 0.468
    yOffset = 0.187
    moveToX1 = round(screen_width * xOffset)
    moveToY1 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # "Accept" Button
    leftTopX = 0.625
    leftTopY = 0.281
    regionW = 0.078
    regionH = 0.406
    image = pyautogui.screenshot(region=(screen_width * leftTopX, screen_height * leftTopY, screen_width * regionW, screen_height * regionH))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # search pattern on screen for accept button
    acceptTask_coordinates = cv2.matchTemplate(image, acceptTask, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(acceptTask_coordinates)
    if max_val < 0.95:
        fishing_task_state = "End" # No task anymore
        # Press ESC
        print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing pet window.")
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        return
    fishing_task_state = "Accepted"
    top_left = max_loc
    w, h = acceptTask.shape[::-1]
    moveToX2 = round(screen_width*leftTopX + top_left[0] + w / 2 + random.randint(-5, 5))
    moveToY2 = round(screen_height*leftTopY + top_left[1] + h / 2 + random.randint(-5, 5))
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX2, y=moveToY2, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Press ESC
    print(strftime("%H:%M:%S", gmtime()), "Pressing ESC, closing pet window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

    time.sleep(random.uniform(2.0, 3.0))


def trySubmitGuildFishingTask(screen_width, screen_height):
    global fishing_task_state
    # "Submit" Button
    leftTopX = 0.8405
    leftTopY = 0.3687
    regionW = 0.03967
    regionH = 0.01567
    max_val = 0
    max_loc = None
    for _ in range(10):
        time.sleep(0.1)
        image = pyautogui.screenshot(region=(screen_width * leftTopX, screen_height * leftTopY, screen_width * regionW, screen_height * regionH))
        image = cv2.cvtColor(numpy.array(image), 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # search pattern on screen for submit button
        submitTask_coordinates = cv2.matchTemplate(image, submitTask, cv2.TM_CCOEFF_NORMED)
        _, mval,_ , mloc = cv2.minMaxLoc(submitTask_coordinates)
        if mval > max_val:
            max_val = mval
            max_loc = mloc
    if max_val < 0.30:
        return
    fishing_task_state = "Try Accept"
    top_left = max_loc
    w, h =submitTask.shape[::-1]
    moveToX1 = round(screen_width*leftTopX + top_left[0] + w / 2 + random.randint(-5, 5))
    moveToY1 = round(screen_height*leftTopY + top_left[1] + h / 2 + random.randint(-5, 5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))
    
    xOffset = 0.18359
    yOffset = 0.6625
    moveToX1 = round(screen_width * xOffset)
    moveToY1 = round(screen_height * yOffset)
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=moveToX1, y=moveToY1, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))
    
def checkFishingTask(screen_width, screen_height):
    global fishing_task_state
    if fishing_task_state == "Try Accept":
        acceptGuildFishingTask(screen_width, screen_height)
        moveCursorToLake(screen_width, screen_height)

    if fishing_task_state == "Accepted":
        trySubmitGuildFishingTask(screen_width, screen_height)
        moveCursorToLake(screen_width, screen_height)

def getMovingArrowRegion(perfect_region):
    return (perfect_region[0] + arrow_region_xOffset, perfect_region[1], arrow_region_width, game_bar_region[1] + game_bar_region[3] - perfect_region[1])

def castNet():
    pyautogui.keyDown("d")
    time.sleep(random.uniform(0.25, 0.55))
    pyautogui.keyUp("d")
    counter = 0
    moving_arrow_region = None
    while counter < 16:
        perfect_zone_loc = pyautogui.locateOnScreen(image=perfect_zone, region=game_bar_region, confidence=0.9)
        if perfect_zone_loc is not None:
            print("perfect zone detected!")
            moving_arrow_region = getMovingArrowRegion(perfect_zone_loc)
            break
        time.sleep(0.5)
        counter += 1
    if moving_arrow_region is None:
        return
    while True:
        arrow_loc = pyautogui.locateOnScreen(image=moving_arrow, region=moving_arrow_region, grayscale=True, confidence=0.7)
        if arrow_loc is not None:
            pyautogui.press("space", 3, interval=0.015)
        esc_loc = pyautogui.locateOnScreen(image=esc_btn, region=esc_btn_region, confidence=0.9, grayscale=True)
        if esc_loc is None:
            print(strftime("%H:%M:%S", gmtime()), "esc button missing! game over!")
            time.sleep(5)
            break
    
    
def checkCastNet():
    loc = pyautogui.locateOnScreen(image=cool_feeling, region=cool_feeling_region, confidence=0.8)
    if loc is None:
        return
    else:
        print("Detect cool feeing buff! Ready for cast net.")
        time.sleep(random.uniform(2,3))
        castNet()

def fishingWorkflow(screen_width, screen_height, counter):
    checkFishingTask(screen_width, screen_height)
    checkCastNet()
    castFishingRod(counter)


while(1):
    idletimer = idletimer + 1
    if flag == "pulled":
        fishingWorkflow(screen_width, screen_height, counter)
        flag = "thrown"
        counter = counter + 1
        
    # screenshot creation
    image = pyautogui.screenshot(region=(screen_width/2 - 100, screen_height/2 - 150, 200, 200))
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # search pattern on screen for exclamation point
    template_coordinates = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
    loc = numpy.where( template_coordinates >= 0.7)

    # Based on the search results, either E is pressed or nothing happens and the cycle repeats
    if len(loc[0]) > 0 and flag == "thrown":
        print(strftime("%H:%M:%S", gmtime()), "Found a fish.")
        idletimer = 0
        time.sleep(random.uniform(0.25, 1.0))

        # Caught fish, press e ingame to reel it in
        pyautogui.keyDown(keybindings['fishing'])
        time.sleep( random.uniform( 0.25, 0.55 ))
        pyautogui.keyUp(keybindings['fishing'])

        flag = "pulled"
        time.sleep(random.uniform(5.5, 7.5))

    # search pattern on screen for buoy
    poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
    poplavok_loc = numpy.where( poplavok_coordinates >= 0.7)
    
    if len(poplavok_loc[0]) == 0 and flag == "pulled":
        fishingWorkflow(screen_width, screen_height, counter)
        flag = "thrown"
        counter = counter + 1

    print(strftime("%H:%M:%S", gmtime()), f"Waiting for a fish. Idle timer: {idletimer}. Recast at 500.")

    if idletimer == 600:
        print(f"Idle timer reached 500. Repairing now.")
        idletimer = 0
        repairFishingRod(screen_width, screen_height)
        moveCursorToLake(screen_width, screen_height)
        # Recast
        fishingWorkflow(screen_width, screen_height, counter)
        flag = "thrown"
        counter = counter + 1
