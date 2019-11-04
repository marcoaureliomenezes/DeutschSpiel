# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:23:48 2019

@author: Marco Menezes
"""
import SpSheet as Sp
import generalFunctions as GF
import texts as txt
from time import sleep
from random import randint

subst = Sp.accessSP("Substantive")
prenoun = Sp.accessSP("Prenomen") 
adj = Sp.accessSP("Adjektiven")

class Nomen:
    def __init__(self, nameOfPlayer):
        self.nameOfPlayer = nameOfPlayer     
    '''
    The choseThema method gets the titles of the Substantive sheet, asks the
    player to choose one and returns this title.
    '''
    def __choseThema(self):   
        themaList = Sp.getTitles(subst)
        titleChosen = Sp.choseTitle(themaList)
        return titleChosen
    '''
    The preNounTypes() method gets the titles of the Prenouns sheet, asks the
    player to choose one or more and returns a list containing the titles
    chosen.
    '''
    def __preNounTypes(self):
        preNounList = Sp.getTitles(prenoun)
        preNounChosen = Sp.choseTitles(preNounList)
        return preNounChosen
    '''
    The listSTPrenouns() method uses the method preNounTypes() to get the list
    of prenoun types chosen. Then it runs through the lines of each prenoun
    type, get the prenouns elements and asks the player to choose which prenouns
    he wants in the game.
    '''
    def __listSTPrenouns2(self):
    
        ender = []
        PNTypeChosen = Nomen.__preNounTypes(self)
        for i in PNTypeChosen:
            PNs = Sp.getSubtitles(prenoun,Sp.refCol(prenoun,i,0),"Genre")
            PNChosen = Sp.choseTitles(PNs)
            dada = (i,PNChosen)
            ender.append(dada)
        return ender

    def __listSTPrenouns(self):
        PNList = []
        ender = Nomen.__listSTPrenouns2(self)
        for j in ender:
            addressType = Sp.refTitle(prenoun,j[0])
            colType = addressType[0][1]
            for k in j[1]:
                line = Sp.refLine(prenoun,k,colType)
                elemList2 = [k,[line,colType]]
                PNList.append(elemList2)
        return PNList
    '''
    The substList1 method creates a list of substantives and returns this list.
    Format of each data of the list = [Gender - Singular - Plural - Translate]
    '''
    def __substList(self):
        substList = []
        adjList = []
        titleChosen = Nomen.__choseThema(self)
        refSub = Sp.refTitle(subst,titleChosen)
        colSub = (refSub[0])[1]
        refAdj = Sp.refTitle(adj,titleChosen)
        colAdj = (refAdj[0])[1]
       
        colTSub = Sp.choseTrans(subst,refSub)
   #    colTAdj = Sp.choseTrans(adj,refAdj) TODO: Just one call to translation
        lineSub = Sp.initLine(subst,colSub,"Noun")
        lineAdj = Sp.initLine(adj,colAdj,"Deutsch")
        
        while Sp.Cell(subst,lineSub,colSub) != '':
            elemList = []
            elemList.append(Sp.Cell(subst,lineSub,colSub+1))
            elemList.append(Sp.Cell(subst,lineSub,colSub))
            elemList.append(Sp.Cell(subst,lineSub,colSub+2))
            elemList.append(Sp.Cell(subst,lineSub,colTSub))
            substList.append(elemList)
            lineSub += 1
        
        while Sp.Cell(adj,lineAdj,colAdj) != '':
            elemList2 = []
            elemList2.append(Sp.Cell(adj,lineAdj,colAdj).lower())
       #     elemList2.append(Sp.Cell(adj,lineAdj,colTAdj).lower())
            adjList.append(elemList2)
            lineAdj += 1
        return [substList,adjList]
    '''

    '''    
    def __findAnswer(self,gender,PNChosen,case):
        retGender = 0
        retCase = 0
        genderlist = ['m','n','f','p']
        caseList = ["Nominativ","Akkusativ","Dativ"]
        for i in range(0,len(caseList)):
            if case == caseList[i]:
                retCase = i+1
        for j in range(0,len(genderlist)):
            if gender == genderlist[j]:
                retGender = j+1
        PN_Data = PNChosen[1] 
        print("PN_Data",PN_Data)
        print("PN_Chosen",PNChosen)
        answerL = PN_Data[0] + retGender
        answerC = PN_Data[1] + retCase
        answer = Sp.Cell(prenoun, answerL,answerC)
        return answer
    '''
    
    '''
    def __findAnswer2(self,gender,PNChosen,case,adjective):
        
        article = PNChosen[0]; retGender = 0; retCase = 0    
        for i in range(0,len(txt.caseList)):
            if case == txt.caseList[i]:     retCase = i+1
            
        for j in range(0,len(txt.genderlist)):
            if gender == txt.genderlist[j]: retGender = j+1
            
        if article == "OHNE ARTIKEL":       answer1 = "-"
        else:
            PN_Data = PNChosen[1]
            answerL = PN_Data[0] + retGender
            answerC = PN_Data[1] + retCase
            answer1 = Sp.Cell(prenoun, answerL,answerC)
        if article in txt.weakList:
            answer2 = adjective + txt.adjWeakDek[retCase-1][retGender-1]
        if article in txt.mixList:
            answer2 = adjective + txt.adjMixedDek[retCase-1][retGender-1]
        if article in txt.strongList:
            answer2 = adjective + txt.adjStrongDek[retCase-1][retGender-1]
        return (answer1 + ' ' + answer2)
    '''

    '''      
    def __playGameGeneral(self,name,substList,Input):
        Score = 0
        if Input == 3:  PN = Nomen.__listSTPrenouns(self)
        else:
            PN1 = "Definite"
 
        while 1:
            GF.jumpLines(30)
            print("Player: " + name + "\nScore: ", Score)
            GF.jumpLines(3)       
            turn = Sp.randList(substList)
            substTurn = substList[turn]
            transl = substTurn[3]
            
            if Input == 1: case = "Nominativ"
            else:          case = txt.listCases[Sp.randList(txt.listCases)]            
            if Input == 3:  i = Sp.randList(PN);  PreN = PN[i]
            else: refPN = Sp.refTitle(prenoun,PN1)
            PreN = [PN1, refPN[0]]           

            pChance = randint(0,3)              
            if pChance == 0:
                nomen = substTurn[2]; gender = "p" 
                lastLetter = nomen[len(nomen)-1]
                print("Nomen:",nomen,"(P) - Ubersetzung:",transl)
                if case == "Dativ":
                    if lastLetter != 'n' and lastLetter != 's':
                        nomen += 'n'
            else:
                nomen = substTurn[1]; gender = substTurn[0]
                print("Nomen:",nomen," - Ubersetzung:",transl)                
            print("Case:",case, "- Artikel:",PreN)    
            playerAnswer = input("answer: ")
            if playerAnswer == "quit":  break
            print("PreN", PreN)
            realAnswer = (Nomen.__findAnswer(self,gender,PreN,case) +' '+ nomen)
            if playerAnswer.lower() == realAnswer.lower():  Score += 1                                  # Sobe pontuação
            else:   print("Falsch,", realAnswer), sleep(3)
        return Score
    '''
    
    '''
    def __playGameWithAdj(self,name,List):
        Score = 0
        substList = List[0]; adjList = List[1]
        PN = Nomen.__listSTPrenouns(self)
        while 1:
            GF.jumpLines(30)
            print("Player: " + name + "\nScore: ", Score)
            GF.jumpLines(3)
            sub = Sp.randList(substList)
            adj = Sp.randList(adjList)
            pn = Sp.randList(PN)
            case = txt.listCases[Sp.randList(txt.listCases)] 
            
            substTurn = substList[sub]       
            adjTurn = adjList[adj]            
            adjekt = adjTurn[0]
            PreN = PN[pn]
            transl = substTurn[3]
            pChance = randint(0,3)
            if pChance == 0:
                nomen = substTurn[2]; gender = "p"
                lastLetter = nomen[len(nomen)-1]
                print("Nomen:",nomen,"(P) - Ubersetzung:",transl)
                if case == "Dativ":
                    if lastLetter != 's' and lastLetter != 'n':
                        nomen += 'n'
            else:
                nomen = substTurn[1]; gender = substTurn[0]
                print("Nomen:",nomen," - Ubersetzung:",transl)
            print("Adjektiv:", adjekt, "\nCase:", case,"- Artikel:",PreN[0])    
            playerAnswer = input("answer: ")           
            if playerAnswer == "quit":  break
           
            realAnswer =  (Nomen.__findAnswer2(self,gender,PreN,case,adjekt) +
                                               ' '+ nomen)
            
            if playerAnswer.lower() == realAnswer.lower(): Score += 1 
            else:   print("Falsch,", realAnswer), sleep(3)
        return Score                                  
    '''
    
    '''            
    def playNomen(self,name):
        while 1:   
            GF.jumpLines(20)
            print(txt.WKNomen); GF.jumpLines(5); print(txt.chosemode)
            mode = Sp.choseTitle(txt.NomenMode)
            if mode == "quit": 
                print("Ende des Nomentraining."); sleep(2); break
            else:
                GF.jumpLines(30)
                print(txt.WKNomen + txt.choseNomenList)
                List = Nomen.__substList(self)
                Input = 1
                Input = txt.NomenMode.index(mode) + 1
                if Input == 4:
                    Nomen.__playGameWithAdj(self,name,List)
                else:
                    substList = List[0]
                    Nomen.__playGameGeneral(self,name,substList,Input)

#------------------------------------------------------------------------------#
'''
player1 = Nomen("Dadaia")
player1.playNomen(player1.nameOfPlayer)

    Função Jogar com Substantivo
    Escolha um modo de jogo:
        1- Treinar genero dos substantivos (Somente der, das, die, die)
            a) Escolha o titulo da lista
            b) Escolha a tradução
                Jogar até dar quit
                Fazer pontuação
                
        2- Treinar Nominativo, acusativo e dativo (Somente artigo definido)
            a) Escolha o titulo da lista
            b) Escolha a tradução
                Jogar até dar quit
                Fazer pontuação
  
        3- Treinar Nominativo, acusativo e dativo com prenomes escolhidos.
            a) Escolha o titulo da lista
            b) Escolha a tradução
                Jogar até dar quit
                Fazer pontuação        
        
        4- Treinar declinação de adjetivo para os casos nominativo, acusativo
        e dativo com prenomes (Definido, indefinido, kein, possessivos) ou sem.
            a) Escolha o titulo da lista
            b) Escolha a tradução
                Jogar até dar quit
                Fazer pontuação
'''    