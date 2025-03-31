# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 17:58:23 2022

@author: Alina
"""
area_1 = (50, 46, 47, 48, 45, 43, 39, 40, 41, 44, 49)
area_2 = (36, 35, 37, 37.1, 42, 38, 33, 34, 32, 31, 30)
area_3 = (28, 27, 25, 26, 22, 21, 21.5, 20, 29)
area_4 = (23, 16, 16.5, 17, 17.5, 18, 18.1, 19)
area_5 = (15, 14, 14.1, 13, 11, 11.1, 11.2, 11.3, 11.5, 10, 12)
area_6 = (6, 8, 9, 7, 5)
area_7 = (2, 4, 3, 1)

class Garage:
    
    def __init__(self):
        #self.time = time
        self.__area = 0
        self.buildingNumber = 0
        self.garages = []
        self.time = 0
        
    
    #get the area designated to that building
    def __findArea(self, building_dict, user_input): #private method
        #get the key from the value in a dictionary
        for i in building_dict:
            if building_dict[i] == user_input:
                self.buildingNumber = i
        
        #see if key matches the area lists
        for i in area_1:
            if self.buildingNumber == i:
                self.__area = 1
            
            else:
                continue
        for i in area_2:
            if self.buildingNumber == i:
                self.__area = 2
               
            else:
                continue 
        for i in area_3:
            if self.buildingNumber == i:
                self.__area = 3
                
            else:
                continue
        for i in area_4:
            if self.buildingNumber == i:
                self.__area = 4
               
            else:
                continue
        for i in area_5:
            if self.buildingNumber == i:
                self.__area = 5
                
            else:
                continue
        for i in area_6:
            if self.buildingNumber == i:
                self.__area = 6
                
            else:
                continue
        for i in area_7:
            if self.buildingNumber == i:
                self.__area = 7
                
            else:
                continue
        return self.__area
    
    def get_area(self, building_dict, user_input):
        return self.__findArea(building_dict, user_input)
        
           
    #get a selection of garages in that area        
    def get_garages(self, area_dict):
        for i in area_dict:
            if area_dict[i] == self.__area:
                self.garages.append(i)
        return self.garages   
    
    def get_name(self, name_dict, user_lot):
        for i in name_dict:
            if str(user_lot) == str(i):
                return name_dict[i]
            
    def get_address(self, address_dict, user_lot):
        for i in address_dict:
            if str(user_lot) == str(i):
                return address_dict[i]
    
   
        
        
        
        
        
        