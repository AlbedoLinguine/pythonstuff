import pyautogui
import keyboard

startScript = False
keyboard.add_hotkey('alt+.', startScript = True)

while(startScript):
    print("started")
    pyautogui.moveTo(1000, 700)
    pyautogui.click()
    pyautogui.press('space')

keyboard.wait('ctrl+0')