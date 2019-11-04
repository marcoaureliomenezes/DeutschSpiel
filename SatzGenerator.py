# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 21:30:23 2019

@author: Marco Menezes
"""

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
                if count2 == 10:    break
            break
    return lista
        a = Verb.__findAnswer(self,"Konjunktiv II + Vergangenheit","Du", "Haben")
        print(a)
        print(GF.simpleAnswer(a))
        b = Verb.__findAnswer(self,"Konjunktiv II + Futur II","Ihr", "Kommen")
        print(b)
        print(GF.simpleAnswer(b))
        c = Verb.__findAnswer(self,"Konjunktiv II + Futur II","Du", "Arbeiten")
        print(c)
        print(GF.simpleAnswer(c))
        d = Verb.__findAnswer(self,"Konjunktiv II + Futur II","Ihr", "An-fordern")
# *Resolve the limit error.
    
    ''' 
            pycharm
            PEP
            docstrings.
    '''  
#Think about something (pontuação)