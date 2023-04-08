from pywinauto import Application#installed
import pyautogui#installed
import keyboard #installed
import time
for x in pyautogui.getAllWindows():  
    print(x.title)
windowName = str(input("Please Enter window name: "))
timer = int(input("Please Enter Lock Time (seconds): "))
timeout = time.time() + timer
for x in pyautogui.getAllWindows():  
        x.minimize()
while timer!=0:
    app = Application().connect(title=windowName)
    window = app.top_window()
    window.set_focus()
    if time.time() > timeout or keyboard.is_pressed('q'):
        break

