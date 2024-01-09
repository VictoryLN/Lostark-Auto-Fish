# -*- coding : utf--8 -*-
import numpy
import pyautogui
import cv2
import time
import random
import yaml
from PIL import Image
import win32gui
import logging

debug = True
DEBUG_BANG_IMG_PATH = "debug/bang.png"
DEBUG_CAUGHT_IMG_PATH = "debug/cought.png"
DEBUG_GUILD_ACCEPT_IMG_PATH = 'debug/guild_accept.png'
DEBUG_COOL_FEELING_IMG_PATH = 'debug/cool_feeling.png'
DEBUG_GAME_BAR_IMG_PATH = 'debug/game_bar.png'
DEBUG_ECS_BTN_PATH = 'debug/esc_btn.png'
DEBUG_ARROW_IMG_PATH = 'debug/arrow.png'
DEBUG_SUBMIT_IMG_PATH = 'debug/submit.png'

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
handler =logging.FileHandler("auto_fish.log", mode='w', encoding='utf-8')
handler.setFormatter(logging.Formatter("%(asctime)s-%(name)s-%(levelname)s: %(message)s"))
logger.addHandler(handler)

def check_hwnd(hwnd):
    title = win32gui.GetWindowText(hwnd)
    logger.info(f"窗口名称: {title}")
    if "命运方舟" not in title:
        logger.warning(f"焦点窗口非命运方舟")
        exit(1)
    
    _, _, w, h = win32gui.GetClientRect(hwnd)
    logger.info(f"窗口分辨率:{w}x{h}")
    if w != 1920 and h != 1080:
        logger.warning(f"分辨率大小非1920x1080")
        exit(1)

def waitForSwitchToLostArk():
    print("5秒内请切换至命运方舟")
    time.sleep(5)

def loadConfig():
    with open("resources/config.yaml", mode="r", encoding="utf-8") as yamlfile:
        config = yaml.safe_load(yamlfile)
    return config

def updatePos(d):
    if isinstance(d,dict):
        if 'position' in d:
            for key in d["position"]:
                logger.debug(f"position change, origin:{d['position'][key]}, modi:{win32gui.ClientToScreen(config['hwnd'], tuple(d['position'][key]))}")
                d['position'][key] = win32gui.ClientToScreen(config["hwnd"], tuple(d["position"][key])) 
        if 'region' in d:
            for key in d['region']:
                logger.debug(f"region change, origin:{d['region']}, modi:{win32gui.ClientToScreen(config['hwnd'],tuple(d['region'][key][:2]))}")
                d['region'][key] = (*win32gui.ClientToScreen(config['hwnd'], tuple(d['region'][key][:2])), d['region'][key][2], d['region'][key][3])
        for value in d.values():
            updatePos(value)

def init(config):
    global fishing_task_state, bang, poplavok, \
        acceptTask, submitTask, perfect_zone, moving_arrow, \
        cool_feeling, esc_btn, cool_feeling,cool_feeling_region,\
        game_bar_region,esc_btn_region, arrow_region_xOffset, \
        arrow_region_height, arrow_region_width, bang_region
    fishing_task_state = "Accepted" if config["task"]["enable"] else "End"
    updatePos(config)
    bang = cv2.imread(config["fishing"]["image"]["bang"], 0)
    poplavok = cv2.imread(config["fishing"]["image"]["poplavok"], 0)
    acceptTask = cv2.imread(config["task"]["image"]["acceptTask"],0)
    submitTask = cv2.imread(config["task"]["image"]["submitTask"],0)
    perfect_zone = Image.open(config["miniGame"]["image"]["perfect_zone"])
    moving_arrow = Image.open(config["miniGame"]["image"]["moving_arrow"])
    cool_feeling = Image.open(config["miniGame"]["image"]["cool_feeling"])

    esc_btn = Image.open(config["miniGame"]["image"]["esc_btn"])
    cool_feeling_region = config["miniGame"]["region"]["cool_feeling"]
    game_bar_region = config["miniGame"]["region"]["game_bar"]
    esc_btn_region = config["miniGame"]["region"]["esc_btn"]
    arrow_region_xOffset = config["miniGame"]["arrow"]["xOff"]
    arrow_region_width = config["miniGame"]["arrow"]["width"]
    arrow_region_height = config["miniGame"]["arrow"]["height"]
    bang_region = config["fishing"]["region"]["bang"]
    logger.debug(f"Config: {config}")

    
def moveCursorToLake():
    # Move cursor to lake
    logger.info("move cursor to lake.")
    x, y = config["fishing"]["position"]["lake"]
    pyautogui.click(x=x, y=y, clicks=0, button='left')

# Function to cast fishing rod ingame
def castFishingRod(count):
    moveCursorToLake()
    logger.info(f"Casting fishing rod. Counter: {count}")
    # Cast fishing rod ingame
    pyautogui.keyDown(config["fishing"]["key"]["fish"])
    time.sleep( random.uniform( 0.25, 0.55 ))
    pyautogui.keyUp(config["fishing"]["key"]["fish"])
    time.sleep( random.uniform(4.5, 6.5))

# Function with all steps to repair the fishing rod through the pet inventory
def repairFishingRod():
    if config["repaire"]["key"]["pet-inventory-modifier"] != None and config["repaire"]["key"]["pet-inventory"]!= '':
        logger.info(f"Opening pet inventory ({config['repaire']['key']['pet-inventory-modifier'].upper()} + {config['repaire']['key']['pet-inventory']}).")
        # Open pet inventory
        pyautogui.keyDown(config["repaire"]["key"]["pet-inventory-modifier"] )
        pyautogui.keyDown(config["repaire"]["key"]["pet-inventory"])
        pyautogui.keyUp(config["repaire"]["key"]["pet-inventory"])
        pyautogui.keyUp(config["repaire"]["key"]["pet-inventory-modifier"])
    else:
        logger.info(f"Opening pet inventory ({config['repaire']['key']['pet-inventory']}).")
        # Open pet inventory
        pyautogui.keyDown(config["repaire"]["key"]["pet-inventory"])
        pyautogui.keyUp(config["repaire"]["key"]['pet-inventory'])

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Small repair button offset
    logger.info("Clicking on Pet Function: remote repair.")

    x, y = config["repaire"]["position"]["small_repaire_btn"]
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair LifeTool offset
    logger.info("Clicking on Repair All button.")
    x, y = config["repaire"]["position"]["life_tool_btn"]
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Repair All offset
    logger.info("Clicking on Repair All button.")
    x, y = config["repaire"]["position"]['repaire_all_btn']
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Repair OK offset
    logger.info("Clicking on OK button.")
    x, y = config["repaire"]["position"]['ok_btn']
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(4.0, 5.0))

    # Press ESC
    logger.info("Pressing ESC, closing repair window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Press ESC
    logger.info("Pressing ESC, closing pet window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

def acceptGuildFishingTask():
    global fishing_task_state
    if config['task']['key']['unas-task'] is not None and config['task']['key']['unas-task-modifier'] != '':
        logger.info(f"Opening Una's task ({config['task']['key']['unas-task-modifier'].upper()} + {config['task']['key']['unas-task']}).")
        # Open Una's task
        pyautogui.keyDown(config['task']['key']['unas-task-modifier'])
        pyautogui.keyDown(config['task']['key']['unas-task'])
        pyautogui.keyUp(config['task']['key']['unas-task'])
        pyautogui.keyUp(config['task']['key']['unas-task-modifier'])
    else:
        logger.info(f"Opening Una's task ({config['task']['key']['unas-task']}).")
        # Open pet inventory
        pyautogui.keyDown(config['task']['key']['unas-task'])
        pyautogui.keyUp(config['task']['key']['unas-task'])

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    logger.info("Clicking on Guild Task.")
    # Guild Task tab button offset
    x, y = config['task']['position']['guild_tab']
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # "Accept" Button
    region = config['task']['region']['accept_btn']
    leftTopX, leftTopY = region[0], region[1]
    image = pyautogui.screenshot(region=region)
    if debug:
        image.save(DEBUG_GUILD_ACCEPT_IMG_PATH)
    image = cv2.cvtColor(numpy.array(image), 0)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # search pattern on screen for accept button
    acceptTask_coordinates = cv2.matchTemplate(image, acceptTask, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(acceptTask_coordinates)
    if max_val < 0.95:
        fishing_task_state = "End" # No task anymore
        # Press ESC
        logger.info("Pressing ESC, closing pet window.")
        pyautogui.keyDown('esc')
        pyautogui.keyUp('esc')
        return
    fishing_task_state = "Accepted"
    top_left = max_loc
    w, h = acceptTask.shape[::-1]
    x = round(leftTopX + top_left[0] + w / 2 + random.randint(-5, 5))
    y = round(leftTopY + top_left[1] + h / 2 + random.randint(-5, 5))
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))

    # Press ESC
    logger.info("Pressing ESC, closing pet window.")
    pyautogui.keyDown('esc')
    pyautogui.keyUp('esc')

    time.sleep(random.uniform(2.0, 3.0))

def trySubmitGuildFishingTask():
    global fishing_task_state
    # "Submit" Button
    region = config['task']['region']['submit_btn']
    leftTopX = region[0]
    leftTopY = region[1]
    max_val = 0
    max_loc = None
    for _ in range(10):
        time.sleep(0.1)
        image = pyautogui.screenshot(region=region)
        if debug:
            image.save(DEBUG_SUBMIT_IMG_PATH)
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
    x = round(leftTopX + top_left[0] + w / 2 + random.randint(-5, 5))
    y = round(leftTopY + top_left[1] + h / 2 + random.randint(-5, 5))
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))
    
    x, y = config["task"]["position"]["ok_btn"]
    pyautogui.click(x=x, y=y, clicks=0, button='left')
    time.sleep(random.uniform(1.0, 1.5))
    pyautogui.click(x=x, y=y, clicks=1, button='left')

    # Sleep random amount of time
    time.sleep(random.uniform(2.0, 3.0))
    
def checkFishingTask():
    global fishing_task_state
    if fishing_task_state == "Try Accept":
        acceptGuildFishingTask()

    if fishing_task_state == "Accepted":
        trySubmitGuildFishingTask()

def getMovingArrowRegion(perfect_region):
    return (perfect_region[0] + arrow_region_xOffset, perfect_region[1], arrow_region_width, game_bar_region[1] + game_bar_region[3] - perfect_region[1])

def castNet():
    pyautogui.keyDown(config["miniGame"]["key"]["net"])
    time.sleep(random.uniform(0.25, 0.55))
    pyautogui.keyUp(config['miniGame']['key']['net'])
    counter = 0
    moving_arrow_region = None
    while counter < 16:
        perfect_zone_loc = pyautogui.locateOnScreen(image=perfect_zone, region=game_bar_region, confidence=0.9)
        if debug:
            pyautogui.screenshot(region=game_bar_region).save(DEBUG_GAME_BAR_IMG_PATH)
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
            if debug:
                pyautogui.screenshot(region=moving_arrow_region).save(DEBUG_ARROW_IMG_PATH)
            pyautogui.press("space", 3, interval=0.015)
        esc_loc = pyautogui.locateOnScreen(image=esc_btn, region=esc_btn_region, confidence=0.9, grayscale=True)
        if debug:
            pyautogui.screenshot(region=esc_btn_region).save(DEBUG_ECS_BTN_PATH)
        if esc_loc is None:
            logger.info("esc button missing! game over!")
            time.sleep(5)
            break
    
def checkCastNet():
    loc = pyautogui.locateOnScreen(image=cool_feeling, region=cool_feeling_region, confidence=0.8)
    if debug:
        pyautogui.screenshot(region=cool_feeling_region).save(DEBUG_COOL_FEELING_IMG_PATH)
    if loc is None:
        return
    else:
        print("Detect cool feeing buff! Ready for cast net.")
        time.sleep(random.uniform(2,3))
        castNet()

def fishingWorkflow(counter):
    checkFishingTask()
    checkCastNet()
    castFishingRod(counter)

def startFishing(config):
    flag = "pulled"
    counter = 1
    while(1):
        if flag == "pulled":
            fishingWorkflow(counter)
            start_time = time.time()
            flag = "thrown"
            counter = counter + 1
            
        # screenshot creation
        image = pyautogui.screenshot(region=bang_region)
        if debug:
            image.save(DEBUG_BANG_IMG_PATH)
        image = cv2.cvtColor(numpy.array(image), 0)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # search pattern on screen for exclamation point
        template_coordinates = cv2.matchTemplate(image, bang, cv2.TM_CCOEFF_NORMED)
        loc = numpy.where( template_coordinates >= 0.65)

        # Based on the search results, either E is pressed or nothing happens and the cycle repeats
        if len(loc[0]) > 0 and flag == "thrown":
            if debug:
                cv2.imwrite(DEBUG_CAUGHT_IMG_PATH, image)
            logger.info("Found a fish.")
            start_time = time.time()
            time.sleep(random.uniform(0.25, 1.0))

            # Caught fish, press e ingame to reel it in
            pyautogui.keyDown(config['fishing']['key']['fish'])
            time.sleep( random.uniform( 0.25, 0.55 ))
            pyautogui.keyUp(config['fishing']['key']['fish'])

            flag = "pulled"
            time.sleep(random.uniform(5.5, 7.5))

        # search pattern on screen for buoy
        poplavok_coordinates = cv2.matchTemplate(image, poplavok, cv2.TM_CCOEFF_NORMED)
        poplavok_loc = numpy.where( poplavok_coordinates >= 0.6)
        
        if len(poplavok_loc[0]) == 0 and flag == "pulled":
            fishingWorkflow(counter)
            start_time = time.time()
            flag = "thrown"
            counter = counter + 1
        if time.time() - start_time > config["fishing"]["idleTimeout"] and flag == "thrown": 
            print(f"Idle timer reached {config['fishing']['idleTimeout']}. Repairing now.")
            if config['repaire']['enable']:
                repairFishingRod()
            flag = "pulled"

def main():
    waitForSwitchToLostArk()
    hwnd = win32gui.GetForegroundWindow()
    check_hwnd(hwnd)
    global config
    config = loadConfig() 
    config["hwnd"] = hwnd
    init(config)
    startFishing(config)

if __name__ == '__main__':
    main()
