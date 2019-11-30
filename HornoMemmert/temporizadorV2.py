# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:45:51 2019

@author: USUARIO
"""

from threading import Timer


class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

def printer():
    print ('ipsem lorem')

t = perpetualTimer(5,printer)
t.start()