# -*- coding: utf-8 -*-
"""
Created on Sun Sep 15 13:47:43 2019

@author: Marco Menezes
"""
import SpSheet as Sp
import time
import random

wortS = Sp.accessSP("WortSchatz") 

class WortSchatz:
    
    '''
    Constructor method without parameters.
    '''
    def __init__(self):
        super().__init__()      
#------------------------------------------------------------------------------#

#------------------------------------------------------------------------------#         
    '''
    ChoseWS method creates a list with the titles from the Wortschatz lists
    that the spreadsheet contains, calls the function choseTitle, in order to
    the player choose what we wants to play an returns the address reference of
    this Wortschatz list.
    '''
    def ChoseWS(self): 
        lista = Sp.gettitles(wortS)
        titleChose = Sp.choseTitle(lista)
        return Sp.refSubTitles(wortS,titleChose)
#------------------------------------------------------------------------------#
    ''' Method CrtSingList() (create a singular list):
        
    '''
    def CrtSingList(self):
        wortList = []
        ref = WortSchatz.ChoseWS(self)
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
        provSub = elem[0].split(' ')
        print(provSub[1] + ", Plural: ", elem[1])
        ans = input("Article: ")
        if ans == provSub[0]:
            return True
        else:
            return False
#------------------------------------------------------------------------------#    
    def verbTraining(self,elem):
        print(elem[0] + ", " + elem[3])
        ans = input("\nPerfekt: ")
        if ans == (elem)[1]:
            return True
        else:
            return False
#------------------------------------------------------------------------------#        
    def adTraining(self,elem):
        ans = input((elem)[0] + "\nSynonym: ")
        wort = WortSchatz.Synonym(self,elem[1])      
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
            print("\n\n")
            while ans != "quit":
                rand = random.randint(0,len(List)-1)
                elem = List[rand]
                if elem[2] == "Substantiv":
                    answer = WortSchatz.subTraining(self,elem)
                    print(answer)
                if elem[2] == "Verb":
                    answer = WortSchatz.verbTraining(self,elem)
                    print(answer)
                if elem[2] == "Adjektiv" or elem[2] == "Adverb":
                    answer = WortSchatz.Synonym(self,elem[1])                    

                ans = input()
'''
TODO:
    1- Training the wortschatz
        a) Choose the wortschatz you want to training
        b) Choose the language you want to see the translations
            Play till the player gives a quit.
            * If the word is a substantive
                asks the gender and the plural
            * If the word is a verb:
                asks the Perfekt 
            * If the word is an adverb or adjective:
                asks the synonym and gives 3 change in the schema "Forca"
                
                
                
TODO2:
    Creates the Score

'''         
#------------------------------------------------------------------------------#
wort = WortSchatz()         