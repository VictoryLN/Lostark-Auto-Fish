import sys

if len(sys.argv) == 1:
    input("fishing keybind: ")
    input("How much energy do you want to spend: ")
elif len(sys.argv) == 2:
    input("How much energy do you want to spend: ")
elif len(sys.argv) == 3:
    print(1)
else:
    exit()
