#Chrome Auto Tabs
#Customize and open all your daily chrome tabs with just one click

from re import X
from tkinter import Button
import pyautogui

#Resolution Settings for mouse customized commands

pyautogui.size()
(1366,768)
pyautogui.position()
(605,750)
pyautogui.click(x=605,y=750)
pyautogui.click(button='left')

#Opens Selected Program 

pyautogui.hotkey('ctrl','n')

#Opens Selected Tabs

pyautogui.click(x=301,y=87)
pyautogui.click(button='left', interval=0.50)

pyautogui.hotkey('ctrl','t')


