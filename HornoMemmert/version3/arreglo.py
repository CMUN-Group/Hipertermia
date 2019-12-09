# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 09:23:24 2019

@author: USUARIO
"""

import re
import requests 
import datetime
from memmertTemporizador import RepeatedTimer as RPT
from time import sleep

DEBUG=True #True Simulate Only False Run
    
def dataMiner(URL,file):
    r = requests.get(URL)
    data = r.text
    dataArray=re.split(': |,',data)
    dateTimeObj=datetime.datetime.now()
    timestampStr = dateTimeObj.strftime("%d/%m/%Y %H:%M:%S.%f")
    textDoc = open(file,'a')
    textDoc.write("%s %s\n"%(timestampStr,dataArray[1]))
    textDoc.close()
    print(dataArray[1])
    
#------------------------------------------------------------------------------
if(DEBUG): URL  = "https://20dicprueba.github.io/temp.html"
if(DEBUG==False): URL  = "http://192.168.100.100/atmoweb?Temp1Read="
file = "pruebaGuardado.txt"
#------------------------------------------------------------------------------

print( "starting...")
rt = RPT(1, dataMiner,URL,file) # it auto-starts, no need of rt.start()

try:
       
    timestop  = 120*60
    timestop1 = 240*60
    timestop2 = 180*60
    
#    #Ingresar la primera temperatura
#    print("30 grados centigrados")
#    if(DEBUG): print ("dummy 30")
#    URLA  = "http://192.168.100.100/atmoweb?TempSet=30" 
#    if(DEBUG==False): r = requests.get(URLA)
#    sleep(timestop)
#------------------------------------------------------------------------------   
    #Ingresar la primera temperatura
#    print("25 grados centigrados")
#    if(DEBUG): print ("dummy 25")
#    URLA  = "http://192.168.100.100/atmoweb?TempSet=25" 
#    if(DEBUG==False): r = requests.get(URLA)
#    #sleep(timestop)
#    sleep(timestop1)
    
    #Ingresar la segunda temperatura
    print("30 grados centigrados")
    if(DEBUG): print ("dummy 30")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=30" 
    if(DEBUG==False): r = requests.get(URLA)
    #sleep(timestop)
    sleep(timestop2)
    
    #Ingresar la tercera temperatura
    print("40 grados centigrados")
    if(DEBUG): print ("dummy 40")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=40" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    #Ingresar la cuarta temperatura
    print("50 grados centigrados")
    if(DEBUG): print ("dummy 50")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=50" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    #Ingresar la quinta temperatura
    print("60 grados centigrados")
    if(DEBUG): print ("dummy 60")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=60" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    #Ingresar la sexta temperatura
    print("70 grados centigrados")
    if(DEBUG): print ("dummy 70")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=70" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    #Ingresar la septima temperatura
    print("80 grados centigrados")
    if(DEBUG): print ("dummy 80")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=80" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    #Ingresar la octava temperatura
    print("90 grados centigrados")
    if(DEBUG): print ("dummy 90")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=90" 
    if(DEBUG==False): r = requests.get(URLA)
    sleep(timestop)
    
    print("20 grados centigrados")
    if(DEBUG): print ("dummy 20")
    URLA  = "http://192.168.100.100/atmoweb?TempSet=20" 
    if(DEBUG==False): r = requests.get(URLA)
    
except KeyboardInterrupt:
  print("Something went wrong")
    
finally:
    rt.stop()
 