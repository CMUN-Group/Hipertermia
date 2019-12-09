# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 12:25:03 2019

@author: nixtropy
"""

# importing the requests library 
import requests 
  
# api-endpoint 
URL = "http://maps.googleapis.com/maps/api/geocode/json"
  
# location given here 
location = "delhi technological university"
  
# defining a params dict for the parameters to be sent to the API 
PARAMS = {'address':location} 
  
# sending get request and saving the response as response object 
r = requests.get(url = URL, params = PARAMS) 
print (r.url)