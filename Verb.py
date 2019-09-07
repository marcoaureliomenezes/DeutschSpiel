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
difficultyMsg = "Wählen Sie eine Schwierigkeitsgrad (Nummer) für das VerbenSpiel:\n\n"
mutterspracheMsg = "\nWählen Sie bitte eine Muttersprache für die Übersetzung:\n\n"
subThemaMsg = "\nWählen Sie bitte eine Nummer für das Untertitel des Spiels:\n\n"
themaMsg = "\nWählen Sie bitte eine Nummer für das Thema des Spiels:\n\n"
firstMsg = "\n\nHallo mein Freund! Herzlich Willkommen zum Spiel von Marco Menezes.\n\n"
deutschspreadsheet = xlrd.open_workbook('Deutsch_Databank.xlsx')
VerbenSheet = deutschspreadsheet.sheet_by_name('Verben')

class Verb():
    def __init__(self):
        pass   
#------------------------------------------------------------------------------#  
    def Cell(self,line,column):
        return VerbenSheet.cell(line,column).value
#------------------------------------------------------------------------------#     
    def refCLabel(self,label):
        count = 0
        while 1:
            if label == Verb.Cell(self,0,count):
                break
            if Verb.Cell(self,0,count) == "end":
                print("Es gibt keine Label heißt", label)
                break
            count += 1
        return count
#------------------------------------------------------------------------------#
    def refSubTitles(self,name):
        lista = []
        for i in range(0,4):
            for j in range(0,100):
                if Verb.Cell(self,i,j) == name:
                    count = 1
                    while Verb.Cell(self,i,j + count) == '':
                        count += 1
                    lista.append([(i,j),count])
        return lista
#------------------------------------------------------------------------------# 
    def numVerbs(self, title):        
        vRef = Verb.refCLabel(self,title)
        for i in range(1,5):
            if Verb.Cell(self,i,vRef+1) == "":
                initLine = i+1
                break
        count = 0
        while(1):
            if Verb.Cell(self,count,vRef) == '':
                finalLine = count
                break
            count += 1
        return [initLine,finalLine]
#------------------------------------------------------------------------------#    

#------------------------------------------------------------------------------#    
    def gettitles(self):
        titleList = []
        for i in range(0,200):
            if Verb.Cell(self,0,i) == 'end':
                break
            if Verb.Cell(self,0,i) != '':
                if Verb.Cell(self,0,i) !='Hilfsverben':
                    titleList.append(Verb.Cell(self,0,i))
        return titleList
#------------------------------------------------------------------------------#
            
######################### ACCESS TO THE DYNAMIC DATABASE #######################   
    def callVerbList(self,level):  
        verbList = []
        translate = Verb.choseTrans(self) 
        if level == lvlList[0]:
            titles = Verb.gettitles(self)
            for title in titles:
                verbList += Verb.createVLC(self,title,translate)
        elif level == lvlList[1]:
            titles = Verb.gettitles(self)
            title = Verb.choseTitle(self,titles)
            verbList = Verb.createVLC(self,title,translate)
        elif level == lvlList[2]:
            titles = Verb.gettitles(self)
            title = Verb.choseTitle(self,titles)
            verbList = Verb.createVLSC(self,title,translate)
        return verbList
        
#------------------------------------------------------------------------------#    
    def createVLC(self, title, translate):
        cRef = Verb.refCLabel(self,title) 
        VList = []
        lList = []
        refSize = Verb.numVerbs(self,title)
        initLine = refSize[0]
        endLine = refSize[1]
        for i in range(initLine,endLine):
            lList = []
            if Verb.Cell(self,i,cRef) != '':
                if Verb.Cell(self,i,cRef+1) != '':
                    lList.append(Verb.Cell(self,i,cRef))
                    lList.append(Verb.Cell(self,i,cRef + translate))
                else:
                    continue
            VList.append(lList)
        return VList
#------------------------------------------------------------------------------#
    def createVLSC(self,title,MT):
        VList = []
        lList = []
        miniList = Verb.choseSubTitle(self,title)
        refList = Verb.refCLabel(self,title)
        for i in range(miniList[0],miniList[1]):
            lList = []
            rL = refList
            lList.append(Verb.Cell(self,i,rL))
            lList.append(Verb.Cell(self,i,rL + MT))
            VList.append(lList)
        return VList
#------------------------------------------------------------------------------#

        
######################### INTERFACE WITH THE GAMER #############################
    def welcome(self):
        print(firstMsg)
        time.sleep(5)
        print(difficultyMsg)
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
            time.sleep(2)
        level = lvlList[int(inputLvl)-1]
        print("Schwierigkeitgrad: ", level)
        time.sleep(2)
        return level
#------------------------------------------------------------------------------#    
    def choseTitle(self, titles):
        print(themaMsg)
        inputThema = 0
        while 1:
            confList = Verb.printEnumList(self,titles)
            inputThema = input("Thema: ")
            if inputThema in confList:
                break
            print(invalidInput) 
            time.sleep(2)
        thema = titles[int(inputThema) - 1]
        print("Thema: ",thema)
        time.sleep(2)
        return thema
#------------------------------------------------------------------------------#    
    def choseSubTitle(self,title):
        tRef = Verb.refCLabel(self,title)
        subTitle = []
        Interval = []
        count = 1
        line = " "
        while(1):
            line = Verb.Cell(self,count,tRef)
            if line == "":
                break
            if Verb.Cell(self,count,tRef+1) == "":
                subTitle.append(Verb.Cell(self,count,tRef))
            count += 1
            
        print(subThemaMsg)
        sTitle = 0
        while 1: 
            confList = Verb.printEnumList(self,subTitle)
            inputST = input("UnterThema: ")
            if inputST in confList:
                break
            print(invalidInput)
            time.sleep(2)
            
        inputST = int(inputST)
        
        if inputST == len(confList):
            print("ta no limite")  #TODO: RESOLVE THIS LIMIT FAST
        else:
            interval = (subTitle[inputST-1],subTitle[inputST])            
            count2 = 3
            line = " "
            while line != "":
                line = Verb.Cell(self,count2,tRef)
                if line == interval[0]:
                    Interval.append(count2+1)
                if line == interval[1]:
                    Interval.append(count2)
                count2 += 1
            return Interval  
#------------------------------------------------------------------------------#
    def choseTrans(self):
        tongue =[]
        tRef = Verb.refSubTitles(self,"Übersetzung")
       # for i in tRef: TODO: CHECK THE TRANSLATE COLUMNS PER TITLE.
       #     print(i[1])
        line = ((tRef[0])[0])[0]
        col = ((tRef[0])[0])[1]
        size = (tRef[0])[1]       
        for i in range(0,size):
            tongue.append(Verb.Cell(self,line+1,col+i))             
        print(mutterspracheMsg)
        inputMT = 0
        while 1:
            confList = Verb.printEnumList(self,tongue)
            inputMT = input("Muttersprache: ")
            if inputMT in confList:
                break
            print(invalidInput)
            time.sleep(2)
                       
        inputMT = int(inputMT)
        print("Muttersprache: ",tongue[inputMT-1])
        time.sleep(2)
        return inputMT
    
################################################################################
player1 = Verb()
level = player1.choseSizeList()
verbList = player1.callVerbList(level)
for i in verbList:
    print(i)
    
    """
    TODO: Put the global strings on the spreadsheet.
    Resolve the limit error.
    Create a function that makes the check up made in all the functions of interface
    Make the lock for the muttersprache, Do you know what is it.
    Create the soluction function (many small functions)
    for many tenses.
    create the functions training and playing
    Make the sketch of the first function wich decides show the verbs (training)
    or play the verbs (excercise)
    Think about something (pontuação)
    Explain on the spreadsheet the suntitiles.
    
    """