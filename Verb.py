# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019

@author: Marco Menezes
"""
import time
import SpSheet as Sp
import texts as txt

verben = Sp.accessSP("Verben")

class Verb():
    
    def __init__(self):
        pass  
      
    '''
    calcula o numero de verbos da lista.
    Motivo:
    '''
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
    
    def cutString(string,n):
        b = ''
        for i in range(0,len(string)-n):
            b += string[i]
        return b
#------------------------------------------------------------------------------#    
    def getInfinitive(self,verb):
        verb = verb.replace('-','')
        return verb.lower()
#------------------------------------------------------------------------------#
            
######################### ACCESS TO THE DYNAMIC DATABASE #######################
    '''
    The callVerbList method receives a level (hard, medium or easy). Based on
    this creates the list of verbs:
      Expert:   All verbs from the list (Unregel- and Regelmäßige verben)
      Medium: Verbs from chosen list (Unregel- or Regelmäßige verben)
      Easy:   
    '''
    def callVerbList(self,level):  
        verbList = []
  #      ref = Sp.refSubTitles(verben,"Unregelmäßige Verben")
  #      translate = Sp.choseTrans(verben,ref) 
        
        if level == txt.lvlList[0]:
            titles = Sp.gettitles(verben)
            for title in titles:
                verbList += Verb.createVLC(self,title,translate)
                
        elif level == txt.lvlList[1]:
            titles = Sp.gettitles(verben)
            title = Verb.choseTitle(self,titles)
            verbList = Verb.createVLC(self,title,translate)
            
        elif level == txt.lvlList[2]:
            titles = Verb.gettitles(self)
            title = Verb.choseTitle(self,titles)
            verbList = Verb.createVLSC(self,title,translate)
        return verbList
        
#------------------------------------------------------------------------------#    
    def createVLC(self, title, translate):
        cRef = Sp.refCLabel(verben,title) 
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
        refList = Sp.refCLabel(verben,title)
        for i in range(miniList[0],miniList[1]):
            lList = []
            rL = refList
            lList.append(Sp.Cell(verben,i,rL))
            lList.append(Sp.Cell(verben,i,rL + MT))
            VList.append(lList)
        return VList
#------------------------------------------------------------------------------#
      
######################### INTERFACE WITH THE GAMER #############################
    def welcome(self):
        print(txt.introdMsg)
        time.sleep(5)
        print(txt.difficultyMsg)
#------------------------------------------------------------------------------#   
    def choseLevel(self):
        Verb.welcome(self)
        while(1):
            confList = Sp.printEnumList(txt.lvlList)
            inputLvl = input("Schwierigkeitgrad: ")
            if inputLvl in confList:
                break
            print(txt.invalidInput)
            time.sleep(2)
        level = txt.lvlList[int(inputLvl)-1]
        print("Schwierigkeitgrad: ", level)
        time.sleep(2)
        return level
#------------------------------------------------------------------------------#    
    def choseTitle(self, titles):
        print(txt.themaMsg)
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
        while(1):
            line = Verb.Cell(self,count,tRef)
            if line == "":
                break
            if Verb.Cell(self,count,tRef+1) == "":
                subTitle.append(Verb.Cell(self,count,tRef))
            count += 1
            
        print(txt.subThemaMsg)
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
    def choseTense(self):
        print(txt.tenseMsg)
        returnList = []
        check = ''
        while check != "quit":
            confList = Sp.printEnumList(self,txt.listTense)
            returnList = []
            print(txt.invalidInput) 
            tense = input("Zeiten: ")
            tense = tense.replace(' ','')
            tenseList = tense.split(',')
            for i in range(0,len(tenseList)):              
                if tenseList[i] not in(confList):
                    break
                elif i == len(tenseList) - 1:
                    check = "quit"
        for j in range(0,len(tenseList)):
            aux = int(tenseList[j])
            returnList.append(listTense[aux -1]) 
        return returnList
    
########################## FINDING ANSWERS #####################################    
#------------------------------------------------------------------------------#
    def captureParts(self,verb,verbList):
        inf = Verb.getInfinitive(self,verb)
        final = inf[len(inf)-2] + inf[len(inf)-1]
        if final == 'en':
            stam = Verb.cutString(inf,2)
        else:
            stam = Verb.cutString(inf,1)
        lastLetter = stam[len(stam)-1]
        if lastLetter in finalCase2:
            final = "et"
        else:
            final = 't'
        a = ''
        b = ''
        init = 'ge'
        #print(stam)
        for i in range(0,len(stam)):
             a += stam[i]
             if a in untrennbarePrefix:
                 init = ''
                 
        for j in range(0,len(stam)):
             b += stam[len(stam)-j-1]
             if b == 'rei':
                 init = ''

        titleRef = Verb.refCLabel(self,verbList)
        colV = titleRef
        verbSearch = "-"
        lineR = 0 
        while verbSearch != "":
            verbSearch = Verb.Cell(self,lineR,colV)
            if verbSearch == verb:
                break
            lineR += 1       
        ref = Verb.refSubTitles(self,"Perfekt")
        col = (((ref[1])[0])[1])
        if verbList == "Unregelmäßige Verben":
            col = (((ref[1])[0])[1])
            auxVerb = Verb.Cell(self,lineR, col)
            auxVerb = auxVerb.capitalize()
            partizipII = Verb.Cell(self,lineR, col+1)
 
        else:
            col = (((ref[2])[0])[1])  
            auxVerb = Verb.Cell(self,lineR, col)
            auxVerb = auxVerb.capitalize()
            partizipII = init + stam + final
        return[auxVerb, partizipII]
#------------------------------------------------------------------------------#
    def regFindAns(self,tense, person, verb):
        inf = verb.lower()
        final = inf[len(inf)-2] + inf[len(inf)-1]
     
        if final == 'en':
            stam = Verb.cutString(inf,2)
        else:
            stam = Verb.cutString(inf,1)
        lastLetter = stam[len(stam)-1]
         
        for i in range(0,len(vetPerson)):
            if vetPerson[i] == person:
                if tense == "Präsens":
                    if lastLetter in finalCase2:
                        return stam + vetPrasens2[i]
                    elif lastLetter in finalCase3:
                        return stam + vetPrasens3[i]
                    else:
                        return stam + vetPrasens1[i]
                elif tense == "Präteritum":
                    if lastLetter in finalCase2:
                        return stam + 'e' + vetPrateritum[i]
                    else:
                        return stam + vetPrateritum[i]
#------------------------------------------------------------------------------#
    def unregFindAns(self,tense, person, verb, verbList):
        
        titleRef = Verb.refCLabel(self,verbList)
        colV = titleRef
        verbSearch = "-"
        lineR = 0 
        while verbSearch != "":
            verbSearch = Verb.Cell(self,lineR,colV)
            if verbSearch == verb:
                break
            lineR += 1       
        if tense == "Präsens":
            ref = Verb.refSubTitles(self,"Präsens")
        elif tense == "Präteritum":
            ref = Verb.refSubTitles(self,"Präteritum")
        if tense == "Konjunktiv II":
            ref = Verb.refSubTitles(self,"Konjunktiv II")
        if verbList == "Unregelmäßige Verben":
            col = (((ref[1])[0])[1])
        elif verbList == "Hilfsverben":
            col = (((ref[0])[0])[1])         
        for i in range(0,len(vetPerson)):
            if person == vetPerson[i]:
                columnR = col + i
                return Verb.Cell(self,lineR,columnR)
    ''' 
            pycharm
            PEP
            docstrings.
    '''                        
#------------------------------------------------------------------------------#
    def findAnswer(self,tense, person, verb, verbList):
        infinitiv = Verb.getInfinitive(self,verb)
        listPart = Verb.captureParts(self,verb,verbList)
        auxVerb = listPart[0]
        partizipII = listPart[1]
        prefix = ''
        brokeVerb = verb.split('-')
        if len(brokeVerb) == 2:
            prefix = brokeVerb[0].lower()
            verb = brokeVerb[1].capitalize()
        if tense == "Präteritum" or tense == "Präsens" or tense == "Konjunktiv II":
            if verbList == "Regelmäßige Verben" : 
                conjVerb =  Verb.regFindAns(self,tense, person, verb)
            
            if verbList == "Unregelmäßige Verben" or verbList == "Hilfsverben": 
                conjVerb = Verb.unregFindAns(self,tense, person, verb, verbList)
            return conjVerb + ' ' + prefix
#------------------------------------------------------------------------------#                           
        if tense == "Futur I":
            auxVerb1 = Verb.findAnswer(self,'Präsens',person,
                                       "Werden","Hilfsverben")
#------------------------------------------------------------------------------#                                       "Werden","Hilfsverben")
            return auxVerb1 + ' ' + infinitiv
        if tense == "Perfekt":
            auxVerb1 = Verb.findAnswer(self,'Präsens',person,
                                       auxVerb,"Hilfsverben")
            return auxVerb1 + ' ' + partizipII
#------------------------------------------------------------------------------#        
        if tense == "Plasquamperfekt":
            auxVerb1 = Verb.findAnswer(self,'Präteritum',person,
                                       auxVerb,"Hilfsverben")
            return auxVerb1 + ' ' + partizipII
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Vergangenheit":
            auxVerb1 = Verb.findAnswer(self,'Konjunktiv II',person,
                                       auxVerb,"Hilfsverben")
            return auxVerb1 + ' ' + partizipII
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Futur I":
            auxVerb1 = Verb.findAnswer(self,'Konjunktiv II',person,
                                       "Werden","Hilfsverben")
            return auxVerb1 + ' ' + partizipII
#------------------------------------------------------------------------------#        
        if tense == "Futur II":       
            auxVerb1 = Verb.findAnswer(self,'Präsens',person,
                                       "Werden","Hilfsverben")   
            return auxVerb1 + ' ' + infinitiv + ' ' + auxVerb.lower()
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Futur II":
            auxVerb1 = Verb.findAnswer(self,'Konjunktiv II',person,
                                       "Werden","Hilfsverben")
            return auxVerb1 + ' ' + partizipII + ' ' + auxVerb.lower()
#------------------------------------------------------------------------------#
        if tense == "Passiv Präsen" :
            auxVerb1 = Verb.findAnswer(self,'Präsens',person,
                                       "Werden","Hilfsverben")
            return auxVerb1 + ' ' + partizipII
#------------------------------------------------------------------------------#        
        if tense == "Passiv Vergangenheit":
            auxVerb1 = Verb.findAnswer(self,'Präteritum',person,
                                       "Werden","Hilfsverben")
            return auxVerb1 + ' ' + partizipII      
################################################################################
    def getList1(self):
        lista = []
        for i in range(0,200):
            if Verb.Cell(self,0,i) == "Verben zu konjugieren jetzt":
                count = 1; count2 = 0        
                while 1:
                    if Verb.Cell(self,count,i) == "":
                        count2 += 1
                    elif Verb.Cell(self,count,i) != "":
                        lista.append(Verb.Cell(self,count,i).capitalize())
                        count2 = 0
                    count += 1
                    if count2 == 10:
                        break
                break
        return lista
################################################################################
    def checkLists(self,v):
        refUnreg = Verb.refCLabel(self,"Unregelmäßige Verben")
        verb = " "
        count = 0
        while 1:
            verb = Verb.Cell(self,count,refUnreg)
            count += 1
            if verb == "":
                break
            if verb == v:
                return "Unregelmäßige Verben"
        refReg = Verb.refCLabel(self,"Regelmäßige Verben")
        verb = " "
        count2 = 0
        while 1:
            verb = Verb.Cell(self,count2,refReg)
            count2 += 1
            if verb == "":
                break
            if verb == v:
                return "Regelmäßige Verben"
            
        return "Wir haben keine Peruanische Verben im Database"
################################################################################
    def printInfo(self,person):
        print("\n\n\n\n\n")
        conf = ["Regelmäßige Verben","Unregelmäßige Verben"]
        lista = Verb.getList1(self)
        for i in lista:
            check = Verb.checkLists(self,i)
            print(i)
            time.sleep(2)
            for j in listTense:
                if check in conf:
                      print(j,"  : ",person,"  ", player1.findAnswer(j, person,
                                                     i,check))
                      time.sleep(1)
                else:
                    print(check)
                    break
            print()
################################################################################
player1 = Verb()
level = player1.choseLevel()
player1.callVerbList(level)
"""
TODO:
*Put the global strings on the spreadsheet.
*Resolve the limit error.
*Create a function that makes the check up made in all the functions of interface
Make the lock for the muttersprache, Do you know what is it.

create the functions training and playing
Make the sketch of the first function wich decides show the verbs (training)
or play the verbs (excercise)
Think about something (pontuação)
"""
