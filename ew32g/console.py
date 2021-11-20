import win32console as w32con
from window import window

class console(window):
    def __init__(self):
        self._hwnd = w32con.GetConsoleWindow()
    def title():
        def fget(self):
            return w32con.GetConsoleTitle()
        def fset(self, value):
            w32con.SetConsoleTitle(str(value))
        def fdel(self):
            pass
        return locals()
    title = property(**title())
console = console()
# console.resize(555,555)
# console.center()
