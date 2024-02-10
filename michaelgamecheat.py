import pyautogui
import keyboard

startScript = False

def startScriptToggle():
    if(startScript): startScript = False
    if(not startScript): startScript = True
    

while(startScript):
    print("started")
    pyautogui.moveTo(1000, 700)
    pyautogui.click()
    pyautogui.press('space')

keyboard.add_hotkey('alt+.', startScriptToggle)

keyboard.wait('ctrl+0')