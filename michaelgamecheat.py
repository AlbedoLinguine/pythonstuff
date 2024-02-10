import pyautogui
import keyboard

startScript = False

def startScriptToggle():
    global startScript
    startScript = not startScript
    if startScript:
        print("started")
    else:
        print("stopped")

while(startScript):
    print("started")
    pyautogui.moveTo(1000, 700)
    pyautogui.click()
    pyautogui.press('space')

keyboard.add_hotkey('alt', startScriptToggle)

keyboard.wait('ctrl+0')