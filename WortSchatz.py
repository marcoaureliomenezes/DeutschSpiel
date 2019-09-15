# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:43 2019

@author: Marco Menezes
"""
from SpSheet import SpSheet

class WortSchatz(SpSheet):
    
    def __init__(self):
        super().__init__()
        
    def ChoseWS(self):
        aba = SpSheet.accessSP("WortSchatz")  
        lista = SpSheet.gettitles(self,aba)
        titleChose = SpSheet.choseTitle(self,lista)
        numElem = SpSheet.numElem(self,aba,titleChose)
        #return SpSheet.refSubTitles(self,aba,titleChose)
        return numElem
    
wort = WortSchatz()
print(wort.ChoseWS())