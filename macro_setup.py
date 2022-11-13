#make sure you have pyautogui install (pip install pyautogui)
import time, pyautogui

time.sleep() #seconds, use for waiting for stuff to load

pyautogui.click() #mouseclick
x,y = 0
pyautogui.click(x,y) #mouseclick on screen at location x,y
print(pyautogui.position()) #console pring where the mouse pointer is at

pyautogui.typewrite('<INPUT>') #type the following String for you
pyautogui.press('KEYS') #press the following keys on your keyboard for you
