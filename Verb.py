# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019

@author: Marco Menezes
"""
import time
import xlrd

lvlList = ("Alle Verben (Expert)","Verben pro Klasse (Medium)",
           "Verben pro Unterklasse (Easy)")
invalidInput = "Bitte geben Sie eine gültige Nummer ein!\n"
deutschspreadsheet = xlrd.open_workbook('Deutsch_Databank.xlsx')
VerbenSheet = deutschspreadsheet.sheet_by_name('Verben')

class Verb():
    def __init__(self):
        pass   
 
    def Cell(self,line,column):
        return VerbenSheet.cell(line,column).value
#------------------------------------------------------------------------------#    

#------------------------------------------------------------------------------#    
    def gettitles(self):
        titleList = []
        for i in range(0,200):
            if Verb.Cell(self,0,i) == 'end':
                break
            if Verb.Cell(self,0,i) != '':
                if Verb.Cell(self,0,i) !='Hilfsverben':
                    tupla = (Verb.Cell(self,0,i), i)
                    titleList.append(tupla)
        return titleList
#------------------------------------------------------------------------------#    

#------------------------------------------------------------------------------#
            
######################### ACCESS TO THE DYNAMIC DATABASE #######################
    
    def callVerbList(self,level):     
        if level == lvlList[0]:
            pass        
        elif level == lvlList[1]:
            inputPar = Verb.paramCreateLists(self)
            Verb.createVLC(self,inputPar[0],inputPar[1])
        elif level == lvlList[2]:
            inputPar = Verb.paramCreateLists(self)
#------------------------------------------------------------------------------#    
    def createVLC(self):
        titles = Verb.gettitles(self)
        title = Verb.choseTitle(self,titles)
        VList = []
        lList = []
    #    linesNum = Verb.numVerbs(self, title)
        initLine = 1  
        endLine = 100
        for i in range(initLine,endLine):
            lList = []
            if Verb.Cell(self,i,title[1]) != '':
                lList.append(Verb.Cell(self,i,int(title[1])))
            else:
                continue
            VList.append(lList)
        return VList 
        
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
#------------------------------------------------------------------------------#    
    def choseTitle(self, titles):

        print("Wählen Sie eine Nummer für das Thema des Spiels!\n\n")
        confList = Verb.printEnumList(self,titles)
        thema = ''
        while thema not in(confList):
            print(invalidInput)            
            thema = input()
        return titles[int(thema) - 1]
#------------------------------------------------------------------------------#

player1 = Verb()
print(player1.createVLC())