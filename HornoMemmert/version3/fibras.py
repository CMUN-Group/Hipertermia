# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 16:39:32 2019

@author: nixtropy
"""

import memmertizer as mem

DEBUG = True

URL  = "http://192.168.100.100/atmoweb?Temp1Read="
file = "10Minutos3.txt"

#mem.dataMiner(URL,file,DEBUG)



rt = mem.RepeatedTimer(1, mem.dataMiner,URL,file,DEBUG)
mem.waitMin(10) 
rt.stop()


#mem.hello("estoy aqui")
#mem.setTemp("20", DEBUG)
#mem.wait(1) 
#print("Cambio temperatura")
#mem.setTemp("30", DEBUG) 
#mem.wait(1) 
#print("Finalizar")