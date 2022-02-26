# lost-ark-auto-fish
OpenCV based Lost Ark fishing bot. <br>
Keypress timings have been randomized to minimize chance of getting caught. Could be bannable if caught, so use at your own risk.

## Install dependencies:
```bash
pip install pyautogui opencv-python numpy
pip install Pillow --upgrade
```

## Usage
Edit `main.py` to set your `fishing_keybind`. <br>
Optionally provice how much `[energy]` you want to spend (assuming 60 energy per successful catch). Will fish until you run out by default.
```bash
python main.py [energy]
```
Switch lost ark into focus window within 5 seconds of running script and make sure your cursor is at fishing spot. <br>


