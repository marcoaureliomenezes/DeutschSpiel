# -*- coding: utf-8 -*-
"""
Created on Tue Sep 10 00:05:06 2019
@author: Marco Menezes
"""
import xlrd
import texts as txt
import random

'''
remDupList(List) function receives as parameter a list and returns the content
of this list without duplicate data.
'''

def randList(List):
    rand = random.randint(0,len(List)-1)
    return rand
    
def remDupList(List):
    lista2 = []
    for i in List:
        if i not in lista2:
            lista2.append(i)
    return lista2
'''
pega uma string e coloca o caractere repl no index indicado

'''
def atString(index,string,repl):
    nString = ''
    for i in range(0,len(string)):
        if i == index:
            nString += repl
        else:
            nString += string[i]
    return nString 
'''
The accessSP(sheet) function receives as parameter the sheet's name and returns
this sheet. 
'''
def accessSP(sheet):
    DeutschSpreadsheet = xlrd.open_workbook('Deutsch_Databank.xlsx')
    Sheet = DeutschSpreadsheet.sheet_by_name(sheet)
    return Sheet
'''
The Cell(sheet,line,column function receives as parameters the sheet's name,
line and column and returns the content of the respective cell. 
'''
def Cell(Sheet,line,column):
    return Sheet.cell(line,column).value
'''
initLine method receives as parameter a column and a preValue (the word in the
cell that  and returns the first value
(word) of that column.
'''
def initLine(sheet,col,preValue):
    count = 0
    while Cell(sheet,count,col) != preValue:
        count += 1
    return count + 1
'''
The printEnumList(List) function receives as parameter a List, prints the list 
content enumered to the player as options to choose and returns a list with
these numbers.
z.B: A list contains 3 options to choose. the function returns the list (1,2,3).
After in the interface functions the player will be restricted to choose one of
these numbers as option. Any other choice will be not accept.
'''    
def printEnumList(List):
    confList = []
    for i in range(0,len(List)):
        print(i+1, "-", List[i])
        confList.append(str(i+1))
    return confList
'''
The refCTitle(sheet,label) function receives as parameters the sheet's name
and a label, both are string variables. Then the function searches for the title
required in the cells and if the label is found it'll be return the column.
'''
def refCTitle(sheet,label):
    count = 0
    while 1:
        if label == Cell(sheet,0,count):
            break
        if Cell(sheet,0,count) == "end":
            print("Es gibt keine Label heißt", label)
            break
        count += 1
    return count
'''
The getSubtitles(sheet,col) function receives as parameter the sheet's name and
a column and runs though the lines. At the end it returns a list containing the
subtitles of that list.
'''

def getSubtitles(sheet,col):
    STList = []
    line1 = initLine(sheet,col,'Genre')
    value = ' '
    while 1:
        value = Cell(sheet,line1,col)
        if value == '':
            break
        if Cell(sheet,line1,col+1) == '':
            STList.append(value)
        line1 += 1
    return STList
'''
The getTitles(sheet) function receives as parameter the name of the sheet and
returns a list containing these titles
'''
def getTitles(sheet):
    titleList = []
    count = 0
    while Cell(sheet,0,count) != 'end':
        if Cell(sheet,0,count) != '':
            titleList.append(Cell(sheet,0,count))
        count += 1
    return titleList
'''
The choseTitle(titles) fuction receives as parameter a list of titles, prints
a message and the options that the player has enumered.  
'''       
def showTitle(titles):
    confirmList = []
    for i in range(0,len(titles)):
        confirmList.append(str(i+1))
        print(str(i+1),"-", titles[i])
    return confirmList

'''
The choseTitle(titles) function is a method of interface. It has as parameter a 
list of titles and asks the player to choose one of the (only one). Finally
it returns the name of the title chosen. 
'''
def choseTitle(titles): 
    thema = ''
    confList = showTitle(titles)  
    while 1:
        thema = input()
        if thema in confList:
            break
        print(txt.invalidInput)
    return titles[int(thema)-1]

'''
The choseTitles(titles) function is similar to the choseTitle, but with the
difference the player can choose more than one title from the list.
'''  
def choseTitles(titles):
    returnList = []
    thema = ''
    confirmList = showTitle(titles)  
    while 1:
        count = 0
        print(txt.invalidInput)            
        thema = input() 
        thema = thema.replace(" ","")
        themaList = thema.split(",")
        themaList = remDupList(themaList)
        for i in themaList:
            for j in confirmList:
                if i == j:
                    count += 1
        if count == len(themaList):
            break
    for i in themaList:
        returnList.append(titles[int(i)-1])                
    return returnList    
#------------------------------------------------------------------------------#
'''
The refSubTitles(sheet,name) function receives as parameter the sheet's name
and the name of the title searched. Then it runs through the lines and columns
and when it found the title it returns a list of 2 elements (address,size).
Address means the coordinate (i,j) and size the width (in number of columns)
of that title. 
'''
def refTitle(sheet,name):
    for i in range(0,40):
        for j in range(0,20):
            if Cell(sheet,i,j) == name:
                size = 1
                while Cell(sheet,i,j + size) == '':
                    size += 1
                    if (Cell(sheet,i+1,j + size) == '' and 
                        Cell(sheet,i+2,j + size) == ''):
                        break
                return [(i,j),size]
'''

'''
def refSubTitleList(sheet,List):
    RefList = []
    for i in range(0,len(List)):
        RefList.append(refTitle(sheet,List[i]))
    return RefList
#------------------------------------------------------------------------------#
'''
The refTrans(sheet,ref) function receives as parameter a sheet and a reference
(a column). Then it gets the parameters of the reference, finds the column
which starts the translation languages and puts the language names contained in
a list called tongue and the respective address (column) of these languages in
a list called tongueAdress.
Finally 
'''
def choseTrans(sheet,ref):
    tongue =[]
    tongueAddr =[]
    line = (ref[0])[0]
    col = (ref[0])[1]   
    lineST = (ref[0])[0] + 1   # Line that contains the subtitles
    lineLang = line + 2        # Line that contains the languages
    size = ref[1]              # Size of the table.
    print(txt.MTMsg)
    for i in range(0,size):
        if Cell(sheet,lineST,col + i) == "Übersetzung":
            count = 0
            tCol = col + i
            while Cell(sheet,lineLang,tCol) != '':                   
                tongueName = Cell(sheet,lineLang,tCol)
                tongue.append((tongueName))
                tongueAddr.append(tCol)
                count += 1
                tCol = col + i + count              
    inputMT = 0
    while 1:
        confList = printEnumList(tongue)
        inputMT = input("Muttersprache: ")
        if inputMT in confList:
            break
        print(txt.invalidInput)                    
    inputMT = int(inputMT)
    return tongueAddr[inputMT-1]
'''
The firstLine(sheet,vref,preValue) receives as parameter the sheet's name, a
column where the table is (ref) and the preValue, that indicates the content
of the cell that precedes the first value of that table.
'''    
def firstLine(sheet,ref,preValue):
    count = 0
    ref = (ref[0])[1]
    zeroValue = ''
    while zeroValue != preValue:
        zeroValue = Cell(sheet,count,ref)
        count += 1
    return count
#------------------------------------------------------------------------------#    
def numElem(aba, vref):        
    for i in range(1,5):
        if Cell(aba, i, vref+1) == "":
            initLine = i+1
            break
    count = 0
    while(1):
        if Cell(aba,count,vref) == '':
            finalLine = count
            break
        count += 1
    return [initLine,finalLine]
#------------------------------------------------------------------------------#
#TODO: 
# Escolher todos
# Tirar na sorte pronome
# Tirar na sorte substantivo
#Tirar na sorte caso    
# Começar a criar modelos de expressões para gerar sentenças  
#Terminar Wortschatz  
# Deklinação de adjetivos  
