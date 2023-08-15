import pyautogui as py
import random
import time

time.sleep(5)

msg=["to testando programa", "boa noite", "to testando bosta em py", "ja vai parar prometo", "perdão lucas"]

while True:
    mesagem=random.choice(msg)
    py.write(mesagem)
    py.press("enter")