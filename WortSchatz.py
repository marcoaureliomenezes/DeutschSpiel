# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:43 2019
@author: Marco Menezes
"""
import SpSheet as Sp
import time
import random
import texts as txt

wortS = Sp.accessSP("WortSchatz") 

class WortSchatz:
    
    #Constructor method without parameters.
    def __init__(self,nameOfPlayer):
        self.nameOfPlayer = nameOfPlayer         
    '''
    ChoseWS method creates a list with the titles from the Wortschatz lists
    that the spreadsheet contains, calls the function choseTitle, in order to
    the player choose what we wants to play an returns the address reference of
    this Wortschatz list.
    '''
    def __ChoseWS(self): 
        lista = Sp.getTitles(wortS)
        titleChose = Sp.choseTitle(lista)
        return Sp.refTitle(wortS,titleChose)
    ''' 
        Method CrtSingList() (create a singular list):  
    '''
    def __CrtSingList(self):
        wortList = []
        ref = WortSchatz.__ChoseWS(self)
        col = (ref[0])[1]
        colT = Sp.choseTrans(wortS,ref)
        colTip = col + 2
        line = Sp.firstLine(wortS,ref,"Singular/Präsens")
        while Sp.Cell(wortS,line,col) != '':
            elemList = []
            elemList.append(Sp.Cell(wortS,line,col))
            elemList.append(Sp.Cell(wortS,line,col+1))
            elemList.append(Sp.Cell(wortS,line,colTip))
            elemList.append(Sp.Cell(wortS,line,colT))
            wortList.append(elemList)
            line += 1
        return wortList
#------------------------------------------------------------------------------#
    def __subTraining(self,elem):
        provSub = elem[0].split(' ')
        print(provSub[1], "- Plural:", elem[1], "\nÜbersetzung:", elem[3])
        playerAnswer = input("Antowort: ").lower()
        realAnswer = (provSub[0] + " " + provSub[1]).lower() 
        return [playerAnswer,realAnswer]
#------------------------------------------------------------------------------#    
    def __verbTraining(self,elem):
        print(elem[0], "- Übersetzung:", elem[3])
        playerAnswer = input("Antwort: ").lower()
        realAnswer = elem[1]
        return [playerAnswer,realAnswer]
#------------------------------------------------------------------------------#    
    def __forca(self,playerAns,synonList,dicaList,word):   
        for l1 in range(0,len(playerAns)):      
            for l2 in range(0,len(synonList[word])):
                if playerAns[l1] == (synonList[word])[l2]:
                    dicaList[word] = Sp.atString(l2,dicaList[word],
                            playerAns[l1]) 
    
    def __Synonym(self,elem):   
        playerAnswer = ''
        synList = []
        dicaList = []
        print(elem[0], "- Übersetzung:", elem[3])
        synon = elem[1].replace(" ","")
        synList = synon.split(",")
        for word in range(0,len(synList)):
            synList[word] = synList[word].lower()

        for word in synList:
            dica = ''
            for letter in range(0,len(word)):
                dica += '-' 
            dicaList.append(dica)     
        count = 3
        while 1:
            if count == 0:
                break
            playerAnswer = input().lower()
            if playerAnswer == "quit":
                break
            for word in range(0,len(synList)):
                if playerAnswer == synList[word]:
                    return True          
                else:
                    WortSchatz.__forca(self,playerAnswer,synList,dicaList,word)
            print(dicaList)      
            count -= 1
#------------------------------------------------------------------------------#
    def __practice(self,name,List):
        score = 0
        print(txt.jNext + txt.infoWS + txt.choseWS)               
        Answers = ['','']
        while 1:
            print(txt.jNext,"Player:",name,"- Score:",score, txt.jScore)
            rand = random.randint(0,len(List)-1)
            elem = List[rand]
            
            if elem[2] == "Substantiv":
                Answers = WortSchatz.__subTraining(self,elem)
                if Answers[0] == Answers[1]:
                    score += 1
                if Answers[0] == "quit":
                    break
                if Answers[0] != Answers[1]:
                    print("\nFalsch,", elem[0])
                    a = input()
            if elem[2] == "Verb":
                Answers = WortSchatz.__verbTraining(self,elem)
                if Answers[0] == Answers[1]:
                    score += 1
                if Answers[0] == "quit":
                    break
                if Answers[0] != Answers[1]:
                    print("\nFalsch,", Answers[1])
                    a = input()
            if elem[2] == "Adjektiv" or elem[2] == "Adverb":
                answer = WortSchatz.__Synonym(self,elem)
                if answer == True:
                    score += 1
            if Answers[0] == "quit":
                    break
    '''
    '''
    def __training(self,name,List):
        for elem in List:
            Input = input()
            if Input == "quit": break
            if elem[2] == 'Verb':
                print(elem[2],': ', elem[0], "- Perfekt:", elem[1],
                      '\nÜbersetzung:', elem[3],"\n\n")               
            if elem[2] == 'Substantiv':
                print(elem[2],': ', elem[0], "- Plural:", elem[1],
                      '\nÜbersetzung:', elem[3],"\n\n")            
            if elem[2] == 'Adjektiv':
                print(elem[2],': ', elem[0],'\nÜbersetzung:', elem[3],"\n\n")
                
    def playWS(self,name):
        print(txt.WStxt + txt.choseWS)
        activity = Sp.choseTitle(txt.WSMode)
        List = WortSchatz.__CrtSingList(self)
        if activity == "Training":
            WortSchatz.__training(self,name,List)
        elif activity == "Übung":
            WortSchatz.__practice(name,List)
        
'''
TODO2: Creates a fair Score
'''         
#------------------------------------------------------------------------------#
wort = WortSchatz("Dadaia")
wort.playWS(wort.nameOfPlayer)