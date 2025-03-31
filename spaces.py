# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:43:12 2022

@author: Alina
"""

class Spaces:
    
    def __init__(self, userInput):
        self.__lotA = 100
        self.__lotC = 20
        self.__lotD = 40
        self.__lotE = 20
        self.__lotF = 30
        self.__lotG = 30
        self.__lotH = 30
        self.__lotJ = 30
        self.__lotK = 60
        self.__lotL = 20
        self.__lotM = 50
        self.__lotO = 30
        self.__lotQ = 15
        self.__lotR = 15
        self.user = userInput
        self.__userLot = 0
    
    def get_spaceNumber(self):
        if self.user == "Lot A":
            self.__userLot = self.__lotA
            return self.__userLot
        elif self.user == "Lot C":
            self.__userLot = self.__lotC
            return self.__lotC
        elif self.user == "Lot D":
            self.__userLot = self.__lotD
            return self.__lotD
        elif self.user == "Lot E":
            self.__userLot = self.__lotE
            return self.__lotE
        elif self.user == "Lot F":
            self.__userLot = self.__lotF
            return self.__lotF
        elif self.user == "Lot G":
            self.__userLot = self.__lotG
            return self.__lotG
        elif self.user == "Lot H":
            self.__userLot = self.__lotH
            return self.__lotH
        elif self.user == "Lot J":
            self.__userLot = self.__lotJ
            return self.__lotJ
        elif self.user == "Lot K":
            self.__userLot = self.__lotK
            return self.__lotK
        elif self.user == "Lot L":
            self.__userLot = self.__lotL
            return self.__lotL 
        elif self.user == "Lot M":
            self.__userLot = self.__lotM
            return self.__lotM
        elif self.user == "Lot O":
            self.__userLot = self.__lotO
            return self.__lotO
        elif self.user == "Lot Q":
            self.__userLot = self.__lotQ
            return self.__lotQ
        elif self.user == "Lot R":
            self.__userLot = self.__lotR
            return self.__lotR
        
    def enter_lot(self):
        if self.user == "Lot A":
            self.__userLot = self.__lotA - 1
            return self.__userLot
        elif self.user == "Lot C":
            self.__userLot = self.__lotC - 1
            return self.__userLot
        elif self.user == "Lot D":
            self.__userLot = self.__lotD - 1
            return self.__userLot
        elif self.user == "Lot E":
            self.__userLot = self.__lotE - 1
            return self.__userLot
        elif self.user == "Lot F":
            self.__userLot = self.__lotF - 1
            return self.__userLot
        elif self.user == "Lot G":
            self.__userLot = self.__lotG - 1
            return self.__userLot
        elif self.user == "Lot H":
            self.__userLot = self.__lotH - 1
            return self.__userLot
        elif self.user == "Lot J":
            self.__userLot = self.__lotJ - 1
            return self.__userLot
        elif self.user == "Lot K":
            self.__userLot = self.__lotK - 1
            return self.__userLot
        elif self.user == "Lot L":
            self.__userLot = self.__lotL - 1
            return self.__userLot
        elif self.user == "Lot M":
            self.__userLot = self.__lotM - 1
            return self.__userLot
        elif self.user == "Lot O":
            self.__userLot = self.__lotO - 1
            return self.__userLot
        elif self.user == "Lot Q":
            self.__userLot = self.__lotQ - 1
            return self.__userLot
        elif self.user == "Lot R":
            self.__userLot = self.__lotR - 1
            return self.__userLot
        
    def exit_lot(self):
        if self.user == "Lot A":
            self.__userLot = self.__lotA + 1
            return self.__userLot
        elif self.user == "Lot C":
            self.__userLot = self.__lotC + 1
            return self.__userLot
        elif self.user == "Lot D":
            self.__userLot = self.__lotD + 1
            return self.__userLot
        elif self.user == "Lot E":
            self.__userLot = self.__lotE + 1
            return self.__userLot
        elif self.user == "Lot F":
            self.__userLot = self.__lotF + 1
            return self.__userLot
        elif self.user == "Lot G":
            self.__userLot = self.__lotG + 1
            return self.__userLot
        elif self.user == "Lot H":
            self.__userLot = self.__lotH + 1
            return self.__userLot
        elif self.user == "Lot J":
            self.__userLot = self.__lotJ + 1
            return self.__userLot
        elif self.user == "Lot K":
            self.__userLot = self.__lotK + 1
            return self.__userLot
        elif self.user == "Lot L":
            self.__userLot = self.__lotL + 1
            return self.__userLot
        elif self.user == "Lot M":
            self.__userLot = self.__lotM + 1
            return self.__userLot
        elif self.user == "Lot O":
            self.__userLot = self.__lotO + 1
            return self.__userLot
        elif self.user == "Lot Q":
            self.__userLot = self.__lotQ + 1
            return self.__userLot
        elif self.user == "Lot R":
            self.__userLot = self.__lotR + 1
            return self.__userLot
        
    def __str__(self):
        return f'The number of spots left in {self.user} is ' + str(self.__userLot) + " spots."
    
    

       
