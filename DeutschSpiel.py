# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 00:47:43 2019

@author: Marco Menezes
"""
import texts as txt
import generalFunctions as GF
import SpSheet as Sp
from Verb import Verb
from Nomen import Nomen
from WortSchatz import WortSchatz


def DeutschSpiel():
    GF.jumpLines(30)
    print(txt.introdMsg)
    name = input("Spielername: ")
    
    while 1:
        GF.jumpLines(20)
        print("Herr", name,"\n", txt.chooseMode)
        mode = Sp.choseTitle(txt.modes)
        
        if mode == "Verben":
            player1 = Verb(name)
            player1.playVerb(player1.nameOfPlayer)     
        if mode == "Nomen":
            player1 = Nomen(name)
            player1.playNomen(player1.nameOfPlayer)  
        if mode == "Wortschatz":
            wort = WortSchatz(name)
            wort.playWS(wort.nameOfPlayer)       
        elif mode == "quit":    print("Ende des Deutschspiels"); break
    
    
DeutschSpiel()