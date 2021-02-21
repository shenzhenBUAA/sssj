import numpy as np
import time
import win32gui, win32ui, win32con, win32api



def get_child_windows(parent):        
    
    if not parent:         
         return      
    hwndChildList = []     
    win32gui.EnumChildWindows(parent, lambda hwnd, param: param.append(hwnd),  hwndChildList)          
    return hwndChildList 


#获取父句柄hwnd类名为clsname的子句柄
hwnd = win32gui.FindWindow(None,'UU 上号器')
#hwnd=win32gui.FindWindow('Notepad',None)
left, top, right, bottom = win32gui.GetWindowRect(hwnd)
print(hwnd)
W_X = right - left
W_Y =  bottom - top
print(W_X,W_Y)

childHwnd = get_child_windows(hwnd)
print(childHwnd)
time.sleep(4)
#win32api.SendMessage(childHwnd[0], win32con.WM_LBUTTONDOWN,0,100)
#win32api.SendMessage(childHwnd[0], win32con.WM_LBUTTONUP,0,100)
x=int((15/100)*W_X)
y=int((40/60)*W_Y)
print(x,y)
lParam = y <<15 | x
win32api.SendMessage(childHwnd[0],win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, lParam);
win32api.SendMessage(childHwnd[0],win32con.WM_LBUTTONUP, 0, lParam);

