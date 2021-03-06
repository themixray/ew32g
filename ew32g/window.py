import win32console as w32con
import win32con as w32c
import win32gui as w32g
import win32api as w32a
import pyautogui as pag

class window:
    def __init__(self, title):
        self._hwnd = w32g.FindWindow(0,title)
    @property
    def hwnd(self):
        return self._hwnd
    def focus(self):
        w32g.BringWindowToTop(self._hwnd)
        w32g.ShowWindow(self._hwnd, w32c.SW_SHOWNORMAL)
        w32g.SetForegroundWindow(self._hwnd)
    def hide(self):
        w32g.ShowWindow(self._hwnd, w32c.SW_HIDE)
    def show(self):
        w32g.ShowWindow(self._hwnd, w32c.SW_SHOW)
    def move(self, x, y):
        x, y = (int(x), int(y))
        w32g.SetWindowPos(self._hwnd,w32c.HWND_TOPMOST,
                          x,y,self.size[0],self.size[1],0)
    def resize(self, width, height):
        width,height=(int(width),int(height))
        w32g.SetWindowPos(self._hwnd,w32c.HWND_TOPMOST,
                          self.position[0],self.position[1],
                          width,height,0)
    def minimize(self):
        w32g.ShowWindow(hwnd, w32c.SW_MINIMIZE)
        return self.size
    def maximize(self):
        w32g.ShowWindow(hwnd, w32c.SW_MAXIMIZE)
        return self.size
    @property
    def title(self):
        return w32g.GetWindowText(self._hwnd)
    @property
    def visible(self):
        return w32g.IsWindowVisible(self._hwnd)
    @property
    def position(self):
        rect = w32g.GetWindowRect(self._hwnd)
        x = rect[0]+7
        y = rect[1]
        return (x, y)
    @property
    def size(self):
        rect = w32g.GetWindowRect(self._hwnd)
        w = rect[2] - self.position[0]-7
        h = rect[3] - self.position[1]-7
        return (w, h)
    def screenshot(self, path):
        rect = self.position+self.size
        self.focus()
        pag.screenshot(path, region=rect)
        return path
    def center(self, x=w32a.GetSystemMetrics(0),
                     y=w32a.GetSystemMetrics(1)):
        self.move(x/2-self.size[0]/2,
                  y/2-self.size[1]/2)
    def destroy(self):
        win32gui.DestroyWindow(self._hwnd)
