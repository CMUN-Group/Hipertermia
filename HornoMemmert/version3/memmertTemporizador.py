# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:24:13 2019

@author: USUARIO
"""

from threading import Timer
#from time import sleep

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer      = None
        self.interval    = interval
        self.function    = function
        self.args        = args
        self.kwargs      = kwargs
        self.is_running  = False
        self.handle_function()
        
    def handle_function(self):
        self.function(*self.args, **self.kwargs)
        self.start()
    
    def start(self):
        self._timer = Timer(self.interval, self.handle_function)
        self._timer.start()

    def stop(self):
        self._timer.cancel() 
        
def hello(name):
    print( "Hello %s!" % name)
        
#rt = RepeatedTimer(1, hello, "World")
#
#try:
#    sleep(10) # your long-running job goes here...
#    
#finally:
#    rt.stop()