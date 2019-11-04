# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019
@author: Marco Menezes
"""
from time import sleep
import SpSheet as Sp
import texts as txt
import generalFunctions as GF

verben = Sp.accessSP("Verben")

class Verb():   
    def __init__(self, nameOfPlayer):
        self.nameOfPlayer = nameOfPlayer     
    
    def numVerbs(self, title):        
        vRef = Sp.refCol(verben,title,0)
        for i in range(1,5):
            if Sp.Cell(verben,i,vRef+1) == "":
                initLine = i+1
                break
        count = 0
        while(1):
            if Sp.Cell(verben,count,vRef) == '':
                finalLine = count
                break
            count += 1
        return [initLine,finalLine]
######################### ACCESS TO THE DYNAMIC DATABASE #######################
    def __callVerbList(self,mode):  
        verbList = []       
################################################################################     
        if mode == txt.VerbMode[0]:
            tonguesList = []
            commonTongues = []
            titles = Sp.getTitles(verben)
                     
            for title in titles:
                ref = Sp.refTitle(verben,title)
                tongues = Sp.getTongueInfos(verben,ref)
                tonguesList.append(tongues[0])
            for i in tonguesList[0]:
                for j in tonguesList[1]:
                    if i == j:
                        commonTongues.append(j)

            print(txt.MTMsg)
            tongue = Sp.choseTitle(commonTongues)
            print("tongue", tongue)
            for j in titles:                 
                verbList += Verb.__createVLC(self,title,translate2)
################################################################################ 
        elif mode == txt.VerbMode[1]:
            titles = Sp.getTitles(verben)
            title = Sp.choseTitle(titles)
            ref = Sp.refTitle(verben,title)
            translate = Sp.choseTrans(verben,ref) 
            verbList = Verb.__createVLC(self,title,translate)
           
        elif mode == txt.VerbMode[2]:
            titles = Sp.getTitles(verben)
            title = Sp.choseTitle(titles)
            ref = Sp.refTitle(verben,title)
            translate = Sp.choseTrans(verben,ref)
            verbList = Verb.__createVLSC(self,title,translate)
        return verbList       
#------------------------------------------------------------------------------#    
    def __createVLC(self, title, translate):
        cRef = Sp.refCol(verben,title,0)
        VList = []; lList = []
        refSize = Verb.numVerbs(self,title)
        initLine = refSize[0]
        endLine = refSize[1]
        for i in range(initLine,endLine):
            lList = []
            if Sp.Cell(verben,i,cRef) != '':
                if Sp.Cell(verben,i,cRef+1) != '':
                    lList.append(Sp.Cell(verben,i,cRef))
                    lList.append(Sp.Cell(verben,i,translate))
                else:
                    continue
            VList.append(lList)
        return VList
#------------------------------------------------------------------------------#
    def __createVLSC(self,title,MT):
        VList = []; lList = []; STList = []; AddList = []        
        colTitle = Sp.refCol(verben,title,0)
        miniList = Sp.getSubtitles(verben,colTitle,"Infinitiv")
        for subTitle in miniList:
            lineTitle = Sp.refLine(verben,subTitle,colTitle)
            STData = [subTitle,[colTitle,lineTitle]]
            STList.append(STData)
        print(txt.subThemaMsg)
        titlesChose = Sp.choseTitles(miniList)
        for i in range(0,len(titlesChose)):
            for j in range(0,len(miniList)):
                if titlesChose[i] == miniList[j]:
                    initLine = STList[j][1][1]; endLine = STList[j+1][1][1]
                    AddList.append([initLine,endLine])
        for elem in AddList:
            firstElem = elem[0] +1; lastElem = elem[1]
            for verb in range(firstElem,lastElem):       
                lList = []
                lList.append(Sp.Cell(verben,verb,colTitle))
                lList.append(Sp.Cell(verben,verb,colTitle + MT))
                VList.append(lList)
        return VList
    #TODO: RESOLVE THIS LIMIT FAST
#------------------------------------------------------------------------------#
    def __choseTense(self):
        print(txt.tenseMsg)
        return Sp.choseTitles(txt.listTense)
    
    def __auxPartizip(self,verb,verbList):
        refTitle = Sp.refTitle(verben,verbList)
        line = refTitle[0][0]; col = refTitle[0][1]; size = refTitle[1]
        lineVerb = Sp.refLine(verben,verb,col)
        if verbList == "Regelmäßige Verben":
            for i in range(0,size):
                if Sp.Cell(verben,line+2,col+i) == "Hilfsverb":
                    colAuxVerb = col+i 
                    auxVerb = Sp.Cell(verben,lineVerb,colAuxVerb)
                    partizipII = GF.Partizip(verb)
                    return[auxVerb, partizipII]                  
        if verbList == "Unregelmäßige Verben":
            for i in range(0,size):
                if Sp.Cell(verben,line+2,col+i) == "Hilfsverb":
                    colAuxVerb = col+i
                if Sp.Cell(verben,line+2,col+i) == "Partizip II":
                    colPart = col+i 
                    auxVerb = Sp.Cell(verben,lineVerb,colAuxVerb)
                    partizipII = Sp.Cell(verben,lineVerb,colPart)
                    return[auxVerb, partizipII]
#------------------------------------------------------------------------------#
    def __RVConjug(self,tense, person, verb):
        verb = verb.lower()
        word = GF.breakWord(verb)
        if len(word) == 2:  inf = word[1];         prefix = word[0]
        else:               inf = verb;             prefix = ''
        stam = GF.stamVerb(inf)
        endLetter = stam[len(stam)-1]
        for i in range(0,len(txt.NomPerson)):
            if txt.NomPerson[i] == person:
                if tense == "Präsens":
                    if endLetter in txt.endCase1:
                        conj = stam + txt.Pras2[i]
                    elif endLetter in txt.endCase2:
                        conj = stam + txt.Pras3[i]
                    else:
                        conj = stam + txt.Pras1[i]                       
                    if prefix == '':    return [conj] 
                    else:               return [conj,prefix]
                    
                elif tense == "Präteritum":
                    if endLetter in txt.endCase1:
                        conj = stam + 'e' + txt.Prat[i]
                    else:
                        conj = stam + txt.Prat[i]
                    if prefix == '':    return [conj] 
                    else:               return [conj,prefix]     
#------------------------------------------------------------------------------#
    def __UVConjug(self,tense, person, verb):
        refTitle = Sp.refTitle(verben,"Unregelmäßige Verben")
        line = refTitle[0][0]; col = refTitle[0][1];
        lineVerb = Sp.refLine(verben,verb,col)
        ref = Sp.refTitle(verben,tense)
        col2 = ref[0][1]
        for i in range(0,len(txt.NomPerson)):
            if person == txt.NomPerson[i]:
                colVerb = col2 + i
                conj = Sp.Cell(verben,lineVerb,colVerb)
        lista = conj.split(" ")
        return lista
#------------------------------------------------------------------------------#
    def __findAnswer(self,tense, person, verb):
        
        verbList = Verb.__checkLists(self,verb)
        if verbList == "Keine verb in Databank!":
            return verbList
        AuxPart = Verb.__auxPartizip(self,verb,verbList)
        auxVerb = AuxPart[0].capitalize();   partizipII = AuxPart[1]
        infinitiv = GF.getInfinitive(verb)
        
        if tense == "Konjunktiv II":
            if verbList == "Unregelmäßige Verben" :          
                conjVerb =  Verb.__UVConjug(self,tense, person, verb)
            return conjVerb
        
        if tense == "Präteritum" or tense == "Präsens":
            if verbList == "Regelmäßige Verben" : 
                conjVerb =  Verb.__RVConjug(self,tense, person, verb)
            
            if verbList == "Unregelmäßige Verben":
                conjVerb = Verb.__UVConjug(self,tense, person, verb)
            return conjVerb
#------------------------------------------------------------------------------#                           
        if tense == "Futur I":
            auxVerb1 = Verb.__findAnswer(self,"Präsens",person, "Werden")
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, infinitiv]
#------------------------------------------------------------------------------#
        if tense == "Perfekt":
            auxVerb1 = Verb.__findAnswer(self,"Präsens",person,auxVerb)
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Plasquamperfekt":
            auxVerb1 = Verb.__findAnswer(self,"Präteritum",person,auxVerb)
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Vergangenheit":
            auxVerb1 = Verb.__findAnswer(self,"Konjunktiv II",person, auxVerb)
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Futur I":
            auxVerb1 = Verb.findAnswer(self,"Konjunktiv II",person, "Werden")
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Futur II":      
            auxVerb1 = Verb.__findAnswer(self, "Präsens", person, "Werden") 
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1,infinitiv,auxVerb.lower()]
#------------------------------------------------------------------------------#        
        if tense == "Konjunktiv II + Futur II":
            auxVerb1 = Verb.__findAnswer(self,"Konjunktiv II", person, "Werden")
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII, auxVerb.lower()]
#------------------------------------------------------------------------------#
        if tense == "Passiv Präsen" :
            auxVerb1 = Verb.__findAnswer(self,"Präsens", person, "Werden")
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Passiv Präteritum":
            auxVerb1 = Verb.__findAnswer(self,'Präteritum',person, "Werden")
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII]
#------------------------------------------------------------------------------#        
        if tense == "Passiv Perfekt":
            auxVerb1 = Verb.__findAnswer(self,'Präsens',person, "Sein")
            auxVerb1 = GF.simpleAnswer(auxVerb1)
            return [auxVerb1, partizipII, "worden"]
################################################################################
    def __checkLists(self,verb):
        refUnreg = Sp.refCol(verben,"Unregelmäßige Verben",0)
        count1 = 2; check = ''        
        while check != "end":
            check = Sp.Cell(verben,count1,refUnreg)
            if check == verb: 
                return "Unregelmäßige Verben"
            count1 += 1            
        refReg = Sp.refCol(verben,"Regelmäßige Verben",0)
        count2 = 2; check = ''
        while check != "end":
            check = Sp.Cell(verben,count2, refReg)
            if check == verb:
                return "Regelmäßige Verben"
            count2 += 1
        return "Keine verb in Databank!"
################################################################################
    def __verbTraining(self,name, verbList,tenseList):
        Score = 0
        while 1:
            GF.jumpLines(30)
            print("Player: " + name + "\nScore: ", Score)
            GF.jumpLines(3)
            verb = verbList[Sp.randList(verbList)]
            person = txt.NomPerson[Sp.randList(txt.NomPerson)]
            tense = tenseList[Sp.randList(tenseList)]
    
            print("Verb:", verb[0], "- Ubersetzung:",verb[1])
            print("Zeit:", tense, "- Person:", person)
            playerAnswer = input("Antwort: ")
            if playerAnswer == "quit":  break
            realAnswerList = Verb.__findAnswer(self,tense,person,verb[0])
            realAnswer = GF.simpleAnswer(realAnswerList)
            if playerAnswer == realAnswer:
                Score += 1
            else:   print("Falsch, ", realAnswer); sleep(3)
     
    def playVerb(self, name):
        while 1:
            GF.jumpLines(30)
            print(txt.WKVerben + txt.chosemode)
            mode = Sp.choseTitle(txt.VerbMode)
            if mode == "quit": 
                print("Ende des Verbentraining."); sleep(2); break
            else:
                verbList = Verb.__callVerbList(self,mode)
                tenseList = Verb.__choseTense(self)
                Verb.__verbTraining(self,name,verbList,tenseList)

################################################################################
'''
player1 = Verb()
player1.generalCall()
'''
#434          goal less than 300
"""
TODO:
* Modal verben
* Questão Konjuntivo com haben e sein e modais
* Create a function that makes the check up made in all the functions of interface
* Make the lock for the muttersprache, Do you know what is it.
create the functions training and playing
Make the sketch of the first function wich decides show the verbs (training)
or play the verbs (excercise)
 
"""
