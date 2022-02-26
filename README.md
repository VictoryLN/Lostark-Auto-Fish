# lost-ark-auto-fish
OpenCV based Lost Ark fishing bot.
Keypress timings have been randomized to minimize chance of getting caught.
Could be bannable if caught, so use at your own risk.

## Install dependencies:
```bash
pip install pyautogui opencv-python numpy
pip install Pillow --upgrade
```

## Usage
Edit `main.py` to set your `fishing_keybind`.
Have Lost Ark open and stand at fishing spot. Switch lost ark into focus window within 5 seconds.
Depending on how much `[energy]` you want to spend (assuming 60 energy per successful catch). Will fish until you run out by default.
```bash
python main.py [energy]
```
