# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 18:27:13 2019

@author: nixtropy
"""
import memmertizer as mem

DEBUG = True
#------------------------------------------------------------------------------
minutes = 1
experimento = {"30" : minutes, 
               "35" : minutes,
               "40" : minutes,
               "45" : minutes,
               "50" : minutes,
               "55" : minutes,
               "60" : minutes,} 
#------------------------------------------------------------------------------
URL  = "http://192.168.100.100/atmoweb?Temp1Read="
file = "pruebaCombo1.txt"
rt = mem.RepeatedTimer(1, mem.dataMiner,URL,file,DEBUG)
#------------------------------------------------------------------------------
for temperatura in experimento:
    mem.setTemp(temperatura, DEBUG)
    mem.waitMin(experimento[temperatura]) 
#------------------------------------------------------------------------------
rt.stop()
