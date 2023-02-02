import pyautogui as pag
import random
import time
import threading


def hareket():
    while True:
        x = random.randint(600, 700)
        y = random.randint(200, 600)
        pag.moveTo(x, y, 0.5)
        time.sleep(0.5)


işlem = threading.Thread(target=hareket, daemon=True)
işlem.start()

yazı = input("To stop pls write. ")
