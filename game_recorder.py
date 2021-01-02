import pyautogui
import numpy as np
import cv2
import time
from listener import Mouse, Keyboard

Original_W = 1360
Original_H = 780
W = Original_W // 4
H = Original_H // 4



def main():
    mouse_listener = Mouse()
    mouse_listener.start()

    keyboard_listener = Keyboard()
    keyboard_listener.start()

    start = time.time()
    for _ in range(100):

        img = pyautogui.screenshot(region=(0, 0, Original_W, Original_H))
        frame = np.array(img)

        frame = cv2.resize(frame, (W, H))

    mouse_listener.stop()
    keyboard_listener.stop()
    print(time.time() - start)


if __name__ == "__main__":
    main()
