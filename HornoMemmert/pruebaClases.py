# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 15:45:51 2019

@author: USUARIO
"""

class Humano:
    def __init__(self, name, age):
        self.name = name
        self.age  = age
        self.start()
        
    def start(self):
        self.age = 25
        print("Estoy aqui")
        
p1 = Humano("holi", 5)
print(p1.name)
print(p1.age)