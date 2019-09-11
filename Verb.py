# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 23:02:21 2019

@author: Marco Menezes
"""
import time
import xlrd

lvlList = ("Alle Verben (Expert)","Verben pro Klasse (Medium)",
           "Verben pro Unterklasse (Easy)")
listTense = ("Präsens","Perfekt","Präteritum","Futur I","Plasquamperfekt",
             "Futur II","Konjunktiv II + Vergangenheit",
             "Konjunktiv II + Futur I","Konjunktiv II + Futur II",
             "Passiv Vergangenheit","Passiv Präsen")
modalVerbs = ("Können","Sollen","Dürfen","Müssen","Wollen")
bitteVerbs = ("Möchten","Würden gern")
untrennbarePrefix = ("be","emp","ent","er","miss","ver","zer")
trennbarePrefix = ("ab","an","auf","aus","bei","ein","mit",
                   "her","hin","vor","weg","zu","zurück")
trennUntrennPrefix = ("durch","hinter","über","um","unter")
vetPerson = ['Ich','Du','Er/Sie/Es','Ihr','Wir/Sie/sie']
invalidInput = "Bitte geben Sie eine gültige Nummer ein!\n"
difficultyMsg = "Wählen Sie eine Schwierigkeitsgrad (Nummer) für das VerbenSpiel:\n\n"
mutterspracheMsg = "\nWählen Sie bitte eine Muttersprache für die Übersetzung:\n\n"
subThemaMsg = "\nWählen Sie bitte eine Nummer für das Untertitel des Spiels:\n\n"
themaMsg = "\nWählen Sie bitte eine Nummer für das Thema des Spiels:\n\n"
introdMsg1 = "\n\nHallo mein Freund! Herzlich Willkommen zum Spiel von Marco"
introdMsg2 = " Menezes. Diese Software hat eine glorreiche Zukunft.\n\n"
introdMsg = introdMsg1 + introdMsg2
tenseMsg1 = "\n\nWählen Sie die im Spiel verfügbaren Zeiten! Geben Sie "
tenseMsg2 = "Kommagetrennte Zahlen, z.B '2,4' for Perfekt und Futur I.\n"
tenseMsg = tenseMsg1 + tenseMsg2
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
    def getInfinitive(self,verb):
        verb = verb.replace('-','')
        return verb.lower()
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
        print(introdMsg)
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
            
        print(subThemaMsg)
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
#------------------------------------------------------------------------------#
    def choseTense(self):
        print(tenseMsg)
        returnList = []
        check = ''
        while check != "quit":
            confList = Verb.printEnumList(self,listTense)
            returnList = []
            print(invalidInput) 
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
        if verbList == "Regelmäßige Verben":
            col = (((ref[2])[0])[1])
        auxVerb = Verb.Cell(self,lineR, col)
        auxVerb = auxVerb.capitalize()
        partizipII = Verb.Cell(self,lineR, col+1)
        return[auxVerb, partizipII]
#------------------------------------------------------------------------------#
    def regFindAns(self,tense, person, verb, verbList):
        infinitiv = verb.lower()
        final = infinitiv[len(infinitiv)-2] + infinitiv[len(infinitiv)-1]
        vetPrasens1 = ['e','st','t','t','en']
        vetPrasens2 = ['e','est','et','et','en']
        vetPrasens3 = ['e','t','t','t','en']
        finalCase2 = ["t","d","m","n"]
        finalCase3 = ["s","x","z","ß"]
        vetPrateritum = ['te','test','te','tet','ten']      
        if final == 'en':
            stam = infinitiv.strip('en')
        else:
            stam = infinitiv.strip('n')
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
                                    
#------------------------------------------------------------------------------#
    def findAnswer(self,tense, person, verb, verbList):
        infinitiv = Verb.getInfinitive(self,verb)
        listPart = Verb.captureParts(self,verb,verbList)
        auxVerb = listPart[0]
        partizipII = listPart[1]
    
        if tense == "Präteritum" or tense == "Präsens" or tense == "Konjunktiv II":
            if verbList == "Regelmäßige Verben" : 
                return Verb.regFindAns(self,tense, person, verb, verbList)
            
            if verbList == "Unregelmäßige Verben" or verbList == "Hilfsverben": 
                return Verb.unregFindAns(self,tense, person, verb, verbList)
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
            auxVerb2prov = Verb.findAnswer(self,'Präsens',person,
                                       auxVerb,"Hilfsverben")     
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
                count = 1
                while Verb.Cell(self,count,i) != "":
                    lista.append(Verb.Cell(self,count,i))
                    count += 1
                break
        return lista

################################################################################
    def printInfo(self):
        lista = Verb.getList1(self)
        print(lista)
        for i in lista:
            print("Verb: " + i)
            for j in listTense:
                print("Ihr", player1.findAnswer(j, "Ihr",i,"Regelmäßige Verben"))

################################################################################
player1 = Verb()
player1.printInfo()
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