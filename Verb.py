# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019

@author: Marco Menezes
"""
import time

lvlList = ("Alle Verben (Expert)","Verben pro Klasse (Medium)",
           "Verben pro Unterklasse (Easy)")
invalidInput = "Bitte geben Sie eine gültige Nummer ein!\n"

class Verb():   
    def __init__(self):
        pass    
######################### INTERFACE WITH THE GAMER #############################
    def welcome(self):
        print("Hallo mein Freund!",
          "Herzlich Willkommen zum Spiel von Marco Menezes.\n\n")
        time.sleep(5)
        print("Wählen Sie eine Schwierigkeitsgrad (Nummer)\n\n")    
#------------------------------------------------------------------------------#    
    def printEnumList(self,List):
        confList = []
        for i in range(0,len(List)):
            print(i+1, "-", List[i])
            confList.append(str(i+1))
        return confList
#------------------------------------------------------------------------------#   
    def choseSizeList(self):
        Verb.welcome(self)
        inputLvl = 0
        while(1):
            confList = Verb.printEnumList(self,lvlList)
            inputLvl = input("Schwierigkeitgrad: ")
            if inputLvl in confList:
                break
            print(invalidInput)
        level = lvlList[int(inputLvl)-1]
        return level
    
