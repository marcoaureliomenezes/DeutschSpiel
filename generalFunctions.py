# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 22:06:09 2019

@author: Marco Menezes
"""
import texts as txt

execptionList = ["bellen"]

def getInfinitive(verb):
    verb = verb.replace('-','')
    return verb.lower()

def cutString(string,n):
    b = ''
    for i in range(0,len(string)-n):
        b += string[i]
    return b

def stamVerb(inf):
    stam = ''
    final = inf[len(inf)-2] + inf[len(inf)-1]
    if final == 'en':
        stam = cutString(inf,2)
    else:
        stam = cutString(inf,1)
    return stam
'''
The breakWord function breaks the trennbare verbs in prefix + verb
'''
def breakWord(inf):
    inf = inf.lower()
    word = []
    for i in range(0,len(inf)):
         if inf[i] == "-":
             word = inf.split("-")
             break
         else:
             word = [inf]
    return word
    
def Partizip(verb):
    verb = verb.lower()
    palavra = breakWord(verb)
    prefix = ''
    if len(palavra) == 2:
        resto = palavra[1]; prefix = palavra[0]
        stam = stamVerb(resto)
    else:
        resto = verb
        stam = stamVerb(resto)

    a = '';b = ''; init = 'ge'
    for i in range(0,len(stam)):
         a += stam[i]
         if a in txt.untrennbarePrefix and verb not in execptionList:
             init = ''        
    for j in range(0,len(stam)):
         b += stam[len(stam)-j-1]
         if b == 'rei':                     init = ''   

    lastLetter = stam[len(stam)-1]
    if lastLetter in txt.endCase1:    final = "et"
    else:                               final = 't'       
    return prefix + init + stam + final  
    
def simpleAnswer(List):
    answer = ''
    for i in range(0,len(List)):
        if i == len(List) -1 :
            answer += List[i]
        else:
            answer += List[i] + " "
    return answer

def jumpLines(number):
    for i in range(0,number):
        print()
             
        