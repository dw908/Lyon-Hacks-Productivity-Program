import win32gui, win32com.client #installed  
from pywinauto import Application#installed
import pyautogui#installed
import win32gui#installed
import win32process#installed
import ctypes#installed
from ctypes import windll
from ctypes import wintypes
import keyboard #installed
import time
import win32api as wapi#installed
import win32con#installed

def windowEnumerationHandler(hwnd, top_windows):
    if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) != '':
        top_windows.append((hwnd, win32gui.GetWindowText(hwnd)))
user32 = ctypes.windll.user32
if __name__ == "__main__":
    results = []
    top_windows = []
    win32gui.EnumWindows(windowEnumerationHandler, top_windows)
    for i in top_windows:
        print (i)
    windowID = int(input("Please Enter window ID: "))
    timer = int(input("Please Enter Lock Time (seconds): "))
    timeout = time.time() + timer
    while timer!=0:
        #win32gui.ShowWindow(i[0],1)
        app = Application(backend='uia').connect(handle=windowID)
       # for i in top_windows:
        #    if str(windowID) in str(i[0]):
         #       window = app.top_window()
          #      window.set_focus()
        if windll.user32.GetForegroundWindow()!= windowID:
            window = app.top_window()
            window.set_focus()
            
        
        if time.time() > timeout or keyboard.is_pressed('esc'):
            break

         #if "notepad" in i[1].lower():
           # print (i)
           # win32gui.ShowWindow(i[0],1)
           # win32gui.SetForegroundWindow(i[0])
           # break
