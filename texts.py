# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 11:33:22 2019

@author: Marco Menezes
"""
#--------------------- DATA ABOUT SUBSTANTIVE CLASS----------------------------#
genderlist = ['m','n','f','p']
caseList = ["Nominativ","Akkusativ","Dativ"]
listCases = ["Nominativ", "Akkusativ","Dativ"]
listGenres = ["Männlich","Neutral","Weiblich","Plural"]

weakList = ["Definite","Dieser","Jener","Derselbe","Derjenige"]
adjWeakDek = [['e','e','e','en'],['en','e','e','en'],['en','en','en','en']]

mixList = ["Indefinite","Kein","Mein","Dein","Sein","Ihr","Unser","Euer"]
adjMixedDek = [['er','es','e','e'],['en','es','e','e'],['en','en','en','en']]

strongList = ["OHNE ARTIKEL"]
adjStrongDek = [['er','es','e','e'],['en','es','e','e'],['em','em','er','en']]

#----------------------- DATA ABOUT VERB CLASS --------------------------------#

listTense = ["Präsens","Perfekt","Präteritum","Futur I","Plasquamperfekt",
             "Futur II","Konjunktiv II + Vergangenheit",
             "Konjunktiv II + Futur I","Konjunktiv II + Futur II",
             "Passiv Vergangenheit","Passiv Präsen"]
listTense2 = ("Präsens","Perfekt","Präteritum")
modalVerbs = ("Können","Sollen","Dürfen","Müssen","Wollen")
bitteVerbs = ("Möchten","Würden gern")
untrennbarePrefix = ("be","emp","ent","er","miss","ver","zer")
trennbarePrefix = ("ab","an","auf","aus","bei","ein","mit",
                   "her","hin","vor","weg","zu","zurück")
Pras1 = ['e','st','t','t','en']
Pras2 = ['e','est','et','et','en']
Pras3 = ['e','t','t','t','en']
endCase1 = ["t","d","m","n"]
endCase2 = ["s","x","z","ß"]
Prat = ['te','test','te','tet','ten'] 
trennUntrennPrefix = ("durch","hinter","über","um","unter")

SubOptions = ["Genre zu trainieren (bestimmter Artikel - Nominativ)",
              "Gender- und Case- Training (bestimmter Artikel - Alle Fälle)",
              "Gender- und Case-Training für ausgewählte Vornamen",
              "Deklination von Vornamen und Adjektiven"]

NomPerson = ['Ich','Du','Er/Sie/Es','Ihr','Wir/Sie/sie']
AkkPerson = ['mich','dich','ihn/sie/es','uns','euch, Sie/sie']
DatPerson = ['mir','dir','ihm/ihr/ihm','uns','euch, Ihnen/ihnen']
RefPerson = ['mich','dich','sich','uns','euch, sich']
#-------------------- DATA ABOUT THE GAME INTERFACE ---------------------------#
#-------------------- DATA ABOUT WORTSCHATZ CLASS   ---------------------------#
WStxt = "Willkommen beim Wortschatz Training und Übung.\n"

infoWS1 = "Vorbildliche Antwort:\n\n"
infoWS2 = "* Verb -> Hilfsverb + Partizip II.\n"
infoWS3 = "* Substantiv -> im Nominativ definierter Artikel.\n"
infoWS4 = "* Adjektiv oder Adverb -> Synonym.\n"
infoWS = infoWS1 + infoWS2 + infoWS3 + infoWS4
#------------------------------------------------------------------------------#
#-------------------- DATA ABOUT NOMEN CLASS ----------------------------------#
Nomentxt = "Willkommen beim Nomen Training (Deklination)\n"

invalidInput = "Bitte geben Sie eine gültige Nummer ein!"
difficultyMsg = "Wählen Sie eine Schwierigkeitsgrad (Nummer) für das VerbenSpiel:\n\n"
MTMsg = "Wählen Sie bitte eine Muttersprache für die Übersetzung:\n"
subThemaMsg = "\nWählen Sie bitte eine Nummer für das Untertitel des Spiels:\n\n"

themaMsg = "\nWählen Sie bitte eine Nummer für das Thema des Spiels:\n\n"
introdMsg1 = "Hallo mein Freund! Herzlich Willkommen zum Spiel von Marco"
introdMsg2 = " Menezes. Diese Software hat eine glorreiche Zukunft.\n"
introdMsg = introdMsg1 + introdMsg2
tenseMsg1 = "\n\nWählen Sie die im Spiel verfügbaren Zeiten! Geben Sie "
tenseMsg2 = "Kommagetrennte Zahlen, z.B '2,4' for Perfekt und Futur I.\n"
tenseMsg = tenseMsg1 + tenseMsg2

chooseMode = "\nWählen Sie bitte eine Mode für das Spiel:\n"
chosemode = "\nWählen Sie bitte eine Trainingsmodus:\n"


WKWS = "Herzlich willkommen beim Wortschatztraining.\n"
choseWS = "\nWählen Sie bitte einen Wortschatz zu trainieren:\n"

WKNomen =  "Herzlich willkommen beim Nometraining (Deklination).\n"
choseNomenList = "\nWählen Sie bitte eines Thema für das Nomentraining:\n"

WKVerben = "Herzlich willkommen beim Verbtraining (Konjugation).\n"

modes = ["Verben","Nomen","Wortschatz","quit"]
WSMode = ["Training","Übung","quit"]
NomenMode = ["Genre (bestimmter Artikel - Nominativ)",
    "Genre und Fall (bestimmter Artikel - Alle Fälle)",
    "Genre und Case (ausgewählte Vornamen - Alle Fälle)",
    "Deklination Vornamen und Adjektiven (ausgewählte Vornamen - Alle Fälle)",
    "quit"]
VerbMode = ["Alle Verben", "Unregelmäßige oder Regelmäße Verben",
            "Ausgewählte Unterlisten", "quit"]