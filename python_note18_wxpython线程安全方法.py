# python_note18wxpython线程安全方法.py
wxpython中3个线程安全函数：
wx.PostEvent
wx.CallAfter
wx.CallLater

import time 
import wx 
     
from threading import Thread 
from wx.lib.pubsub import Publisher

######################################################################## 
class TestThread(Thread): 
    """Test Worker Thread Class."""
     
    #---------------------------------------------------------------------- 
    def __init__(self): 
        """Init Worker Thread Class."""
        Thread.__init__(self) 
        self.start()    # start the thread 
     
    #---------------------------------------------------------------------- 
    def run(self): 
        """Run Worker Thread."""
        # This is the code executing in the new thread. 
        for i in range(6): 
            time.sleep(10) 
            wx.CallAfter(self.postTime, i) 
        time.sleep(5) 
        wx.CallAfter(Publisher().sendMessage, "update", "Thread finished!") 
     
    #---------------------------------------------------------------------- 
    def postTime(self, amt): 
        """
        Send time to GUI
        """
        amtOfTime = (amt + 1) * 10
        Publisher().sendMessage("update", amtOfTime) 

        