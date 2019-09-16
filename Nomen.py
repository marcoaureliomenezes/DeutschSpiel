# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:23:48 2019

@author: Marco Menezes
"""
from SpSheet import SpSheet


class Nomen(SpSheet):
    
    def __init__(self):
        super().__init__()
      
    def getTitles(self):
        aba = SpSheet.accessSP("Nomen")  
        lista = SpSheet.gettitles(self,aba)
        return SpSheet.choseTitle(self,lista)
    

    
        
player1 = Nomen()
#print(player1.getTitle())
print(player1.getTitles())
