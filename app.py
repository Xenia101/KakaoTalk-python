import win32con
import win32api
import win32gui
import time

def loginCheckHnd(whnd):
    if (whnd == 0):
        print("Please login KakaoTalk.. ")
        return

def FindChatroom(chatroom):
    whnd = win32gui.FindWindow(None, "카카오톡")
    loginCheckHnd(whnd)
    whnd_OnlineMainView = win32gui.FindWindowEx(whnd, None, "EVA_ChildWindow", None)
    whnd_ContactListView = win32gui.FindWindowEx(whnd_OnlineMainView, None, "EVA_Window", None)
    whnd_ChatRoomListView = win32gui.FindWindowEx(whnd_OnlineMainView, whnd_ContactListView, "EVA_Window", None)
    whnd_MessageBox = win32gui.FindWindowEx( whnd_ChatRoomListView, None, "Edit", None)

    win32api.SendMessage(whnd_MessageBox, win32con.WM_SETTEXT, 0, chatroom)
    time.sleep(1)
    win32api.PostMessage(whnd_MessageBox, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.5)
    win32api.PostMessage(whnd_MessageBox, win32con.WM_KEYUP, win32con.VK_RETURN, 0)
    time.sleep(1)

def SendMessage(chatroom, text):
    if not isinstance(text, str): text = str(text)
    whndMain = win32gui.FindWindow(None, chatroom)
    loginCheckHnd(whndMain)
    whndChild = win32gui.FindWindowEx(whndMain, None, "RICHEDIT50W", None)
    
    win32api.SendMessage(whndChild, win32con.WM_SETTEXT, 0, text)
    win32api.PostMessage(whndChild, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    time.sleep(0.5)
    win32api.PostMessage(whndChild, win32con.WM_KEYUP, win32con.VK_RETURN, 0)

if __name__ == "__main__":
    chatroom = ""
    message = "Hello World!"
    FindChatroom(chatroom)
    for msg in [x for x in message]:
        SendMessage(chatroom, msg)


