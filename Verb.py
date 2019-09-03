# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019

@author: Marco Menezes
"""

lvlList = ("Alle Verben (Expert)","Verben pro Klasse (Medium)",
           "Verben pro Unterklasse (Easy)")

class Verb():   
    def __init__(self):
        pass
    
######################### INTERFACE WITH THE GAMER ##### #######################
    def printEnumList(self,List):
        confList = []
        for i in range(0,len(List)):
            print(i+1, "-", List[i])
            confList.append(str(i+1))
        return confList
    
    