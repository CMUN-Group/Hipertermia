# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 16:24:13 2019

@author: USUARIO
"""

import requests 
import re
import datetime
from threading import Timer
from time import sleep

class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer      = None
        self.interval    = interval
        self.function    = function
        self.args        = args
        self.kwargs      = kwargs
        self.is_running  = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False 
    
def setTemp(temp, DEBUG):
    if (DEBUG):
        print ("Este es un valor de prueba para " + temp + " grados celsius")
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
            
def dataMiner(URL, file, DEBUG):
    if(DEBUG): URL  = "https://20dicprueba.github.io/temp.html"
    if(DEBUG==False): URL = URL
    try:
        r = requests.get(URL)
        data = r.text
        dataArray=re.split(': |,',data)
        dateTimeObj=datetime.datetime.now()
        timestampStr = dateTimeObj.strftime("%d/%m/%Y %H:%M:%S.%f")
        textDoc = open(file,'a')
        textDoc.write("%s %s\n"%(timestampStr,dataArray[1]))
        textDoc.close()
        print(dataArray[1])
    except requests.exceptions.ConnectionError as e:
            print ("No se pudo realizar la conexión")
            print (e)

    
def waitMin(minutes):
    sleep(minutes*60)

def waitSec(seconds):
    sleep(seconds)
            
def hello(name):
    print( "Hello %s!" % name)
    