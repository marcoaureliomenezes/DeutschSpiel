# -*- coding: utf-8 -*-
"""
Created on Sat Sep 14 00:23:48 2019

@author: Marco Menezes
"""
import SpSheet as Sp
import texts as txt
from random import randint

subst = Sp.accessSP("Substantive")
prenoun = Sp.accessSP("Prenomen") 

class Nomen:
    
    def __init__(self, nameOfPlayer):
        self.nameOfPlayer = nameOfPlayer
        
    '''
    The choseThema method gets the titles of the Substantive sheet, asks the
    player to choose one and returns this title.
    '''
    def choseThema(self):   
        themaList = Sp.gettitles(subst)
        titleChosen = Sp.choseTitle(themaList)
        return Sp.refTitle(subst,titleChosen)
    '''
    The preNounTypes() method gets the titles of the Prenouns sheet, asks the
    player to choose one or more and returns a list containing the titles
    chosen.
    '''
    def preNounTypes(self):
        preNounList = Sp.getTitles(prenoun)
        preNounChosen = Sp.choseTitles(preNounList)
        return preNounChosen
    '''
    The listSTPrenouns() method uses the method preNounTypes() to get the list
    of prenoun types chosen. Then it runs through the lines of each prenoun
    type, get the prenouns elements and asks the player to choose which prenouns
    he wants in the game.
    '''
    def listSTPrenouns(self):
        returnList1 = []
        returnList2 = []
        preNounChosen = Nomen.preNounTypes(self)      
        for i in preNounChosen:
            List = Sp.getSubtitles(prenoun,Sp.refCTitle(prenoun,i))
            List2 = Sp.choseTitles(List)
            List2Addr = Sp.refSubTitleList(prenoun,List2)
            for j in List2:
                returnList1.append(j)
            for k in List2Addr:
                returnList2.append(k[0])
                           
        return [returnList1,returnList2]
    '''
    
    '''
    def randomFeatures(self,PNList):
        PNList = Nomen.listSTPrenouns(self)
        for m in range(0,10):
            i = randint(0,len(PNList[0])-1)
            j = randint(0,len(txt.listGenres)-1)
            k = randint(0,len(txt.listCases)-1)
            addressRef = PNList[1][i]
            answerL = addressRef[0]+1+j
            answerC = addressRef[1]+1+k
            PN = PNList[0][i]
            gender = txt.listGenres[j]
            case = txt.listCases[k]
            answer = Sp.Cell(prenoun, answerL,answerC)
            return [PN,gender,case,answer]
    '''
    The substList1 method creates a list of substantives and returns this list.
    Format of each data of the list = [Gender - Singular - Plural - Translate]
    '''
    def substList1(self):
        substList = []
        ref = Nomen.choseThema(self)
        col = (ref[0])[1]

        colT = Sp.choseTrans(subst,ref)
        line = Sp.initLine(subst,col,"Noun")
        
        while Sp.Cell(subst,line,col) != '':
            elemList = []
            elemList.append(Sp.Cell(subst,line,col+1))
            elemList.append(Sp.Cell(subst,line,col))
            elemList.append(Sp.Cell(subst,line,col+2))
            elemList.append(Sp.Cell(subst,line,colT))
            substList.append(elemList)
            line += 1
        return substList  
    # Função que cria lista com todos os substantivos   
    # função para escolher quais pronomes poderão ser escolhidos na sorte  
    # função que escolhe a na sorte um prenome
'''
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

'''
Função Criar todas as possibilidades para Satz generator
    
    '''
    
    def startSubstGame(self):
        print(txt.difficultyMsg)
        
      
player1 = Nomen("Dadaia")
print("Player:",player1.nameOfPlayer)
player1.randomFeatures()
    