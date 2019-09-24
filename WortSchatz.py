# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:43 2019

@author: Marco Menezes
"""
from SpSheet import SpSheet
import time
import random

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
        col = (ref[0])[1]
        colT = SpSheet.choseTrans(self,aba,ref)
        colTip = col + 2
        line = SpSheet.firstLine(self,aba,ref,"Singular/Präsens")

        while SpSheet.Cell(self,aba,line,col) != '':
            elemList = []
            elemList.append(SpSheet.Cell(self,aba,line,col))
            elemList.append(SpSheet.Cell(self,aba,line,col+1))
            elemList.append(SpSheet.Cell(self,aba,line,colTip))
            elemList.append(SpSheet.Cell(self,aba,line,colT))
            wortList.append(elemList)
            line += 1
        return wortList
#------------------------------------------------------------------------------#   
    def printList(self,List):
        for elem in List:
            if elem[2] == 'Verb':
                print(elem[2],': ', elem[0], "- Perfekt:", elem[1],
                      '\nUbersetzung:', elem[3],"\n\n")
                input()                
            if elem[2] == 'Substantiv':
                print(elem[2],': ', elem[0], "- Plural:", elem[1],
                      '\nUbersetzung:', elem[3],"\n\n")
                input()             
            if elem[2] == 'Adjektiv':
                print(elem[2],': ', elem[0],'\nUbersetzung:', elem[3],"\n\n")
                input()
#------------------------------------------------------------------------------#
    def subTraining(self,elem):
        ans = input(elem[1] + ": ")
        if ans == elem[0]:
            return True
        else:
            return False
#------------------------------------------------------------------------------#    
    def verbTraining(self,elem):
        ans = input((elem)[0] + "\nPerfekt: ")
        if ans == (elem)[1]:
            return True
        else:
            return False
#------------------------------------------------------------------------------#        
    def adTraining(self,elem):
        ans = input((elem)[0] + "\nSynonym: ")
        if ans == (elem)[1]:
            return True
        else:
            return False       
#------------------------------------------------------------------------------#        
    def atString(self,index,string,repl):
        nString = ''
        for i in range(0,len(string)):
            if i == index:
                nString += repl
            else:
                nString += string[i]
        return nString 
#------------------------------------------------------------------------------#    
    def Synonym(self,wort):
        wort = wort.lower()
        dica = ''
        entrada = ''
        for i in range(0,len(wort)):
            dica += '-'
        print(dica)
        while entrada != wort:
            entrada = input().lower()
            if entrada == "quit":
                break 
            for l1 in range(0,len(entrada)):      
                for l2 in range(0,len(wort)):
                    if entrada[l1] == wort[l2]:
                        dica = atString(l2,dica,wort[l2])                   
            print(dica)
            if dica == wort:
                break
        return wort
#------------------------------------------------------------------------------#
    def training(self,List):         
            ans = ''
            while ans != "quit":
                rand = random.randint(0,len(List)-1)
                elem = List[rand]
                if elem[2] == "Substantiv":
                    provSub = elem[0].split(' ')
                    answer = WortSchatz.subTraining(self,provSub)
                    print(answer)
                if elem[2] == "Verb":
                    answer = WortSchatz.verbTraining(self,elem)
                    print(answer)
                if elem[2] == "Adjektiv" or elem[2] == "Adverb":
                    answer = WortSchatz.adTraining(self,elem)
                    print(answer)
                else:
                    print(List[rand])
                ans = input()
    '''
            TODO: 
                * Always print the translation in front of the word before to
                make the question about perfekt, gender, plural or synonym.
                * Quit to the Method printList()               
                * Exercise about gender and plural
                * synonyms game (put to work)
                * Perfekt game
                * Put synonyms in the spreadsheet for wortschatz 1 to 3
                * Complement specifications of the verbs on the spreadsheet
                (akk, dat, reflex) (preposition).
                * Create the function that manage the class Wortschatz()
                * Create Score of the game
                * Make the commit commit
    '''         
#------------------------------------------------------------------------------#
wort = WortSchatz()
for i in range(0,1):
    WortList = wort.CrtSingList()
    wort.training(WortList)
            