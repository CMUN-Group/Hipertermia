# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:44:03 2019

@author: nixtropy
"""

import requests 
from time import sleep

def setTemp(temp, DEBUG):
    if (DEBUG):
        print ("Este es un valor de prueba para " + temp + " grados celcius")
    else: 
        URL = "http://192.168.100.100/atmoweb"  
        temperatura = temp 
        PARAMS = {"TempSet":temperatura}     
        try:
            r = requests.get(url = URL, params = PARAMS) 
            print (r.url)
        except requests.exceptions.ConnectionError as e:
            print ("No se pudo realizar la conexión")
            print (e)

        
setTemp("50", True) 
print("acabe")   

