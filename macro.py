import pyautogui
import time

print(pyautogui.size())
# pyautogui.moveTo(100,100, duration=0.2)

# pyautogui.moveRel(100, 100)
# pyautogui.drag
# pyautogui.dragRel
# pyautogui.scroll(-200)

# pyautogui.click()pi - press once
# pyautogui.press('enter') - press once
# pygautogui.press('f1') - press once
# pyautogui.keyDown('shift') - holds shift down
# pygautogui.keyUp('shift') - releases shift
# pyautogui.hotkey('ctrl, shift, esc') - hotkey(makes you hold all keys til end then release)
# hold() - check pyautogui docs

# pyautogui.alert(text='test', title='something', button='done')

getPrompt = pyautogui.prompt("please choose a prompt: 'test', ")
pyautogui.alert(getPrompt)
