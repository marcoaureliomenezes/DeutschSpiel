# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:43 2019

@author: Marco Menezes
"""
from SpSheet import SpSheet

aba = SpSheet.accessSP("WortSchatz") 

class WortSchatz(SpSheet):
    
    def __init__(self):
        super().__init__()
#------------------------------------------------------------------------------#        
    def cell():
        pass
#------------------------------------------------------------------------------# 
    def initLine(self,col):
        count = 0
        while SpSheet.Cell(self,aba,count,col) != "Singular/Präsens":
            count += 1
        return count + 1
            
#------------------------------------------------------------------------------#         
    def ChoseWS(self): 
        lista = SpSheet.gettitles(self,aba)
        titleChose = SpSheet.choseTitle(self,lista)
        print(titleChose)
        return SpSheet.refSubTitles(self,aba,titleChose)
#------------------------------------------------------------------------------#
    ''' Method CrtSingList() (create a singular list):
        
    '''    
    def CrtSingList(self):      
        wortList = []
        ref = WortSchatz.ChoseWS(self)
        colT = SpSheet.choseTrans(self,aba,ref)
        col = ((ref[0])[0])[1]       
        line = 3
        while SpSheet.Cell(self,aba,line,col) != '':
            wortList.append(SpSheet.Cell(self,aba,line,col))
            wortList.append(SpSheet.Cell(self,aba,line,colT))
            line += 1
        return wortList
#------------------------------------------------------------------------------#        
'''
    TODO: * Put in List the Kind of word (Verb, Adjektiv ...)
          * Put a list inside a list.
          * Function that observes the kind of the word and print (Plural,
          Perfekt, Synonym)
          * Function that prints the wors from the Wortschtz
          * Exercise to training Perfekt or Gender 
'''
wort = WortSchatz()
for i in range(0,1):
    print(wort.CrtSingList())