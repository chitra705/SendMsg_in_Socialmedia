import pyautogui as pg 
import time
 
print("prgm run after 5 second")
time.sleep(5)
print("Running")

for i in range(0,17):
    pg.write("chithu")
    time.sleep(0.5)
    pg.press('Enter')
