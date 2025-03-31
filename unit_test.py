# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 20:31:37 2022

@author: Alina
"""
import pandas as pd
import unittest
from Garage import Garage

#read the excel file of parking lot details
data = pd.read_excel(r'Final_Project_ParkingLotDetail.xlsx')


buildings = {
    16: 'boston university academy',
    25: 'college of arts & science',
    33: 'college of communications',
    32: 'college of engineering',
    14: 'college of fine arts',
    13: 'college of general studies',
    27: 'graduate school of arts & sciences',
    20: 'metropolitan college & extended education',
    35: 'sargent college of health & rehabilitation sciences',
    36: 'school of education',
    7: 'school of hospitality administration',
    19: 'school of law',
    41: 'school of management',
    26: 'school of social work',
    21: 'school of theology',
    21.5: 'university professor programs',
    6: 'agganis arena',
    48: 'barnes & noble at boston university',
    3: 'case athletic center',
    8: 'fitness & recreation center',
    17: 'george sherman union',
    22: 'marsh chapel',
    18: 'mugar memorial library',
    16.5: 'student activities center',
    1: 'track & tennis center',
    28: 'tsai performance center',
    9: '10 buick street', 
    44: '575 commonwelath avenue',
    2: '1019 commonwealth avenue danielsen hall',
    50: 'myles standish hall', 
    45: 'shelton hall',
    24: 'south campus',
    39: 'the towers',
    30: 'warren towers',
    4: 'west campus',
    43: 'admissions reception center',
    5: 'boston university police',
    12: 'center for english language and orientation programs',
    11: 'comptroller',
    17.5: 'dean of students',
    11.5: 'financal assistance',
    49: 'hotel commonwalth',
    10: 'housing office',
    31: 'information technology',
    46: 'international students & scholars office',
    34: 'life science & engineering',
    42: 'metcalf science center',
    40: 'presidents office',
    11.1: 'registrar',
    11.2: 'student health services',
    47: 'university computers',
    11.3: 'university service center',
    14.1: 'bu art gallery at the stone gallery',
    37: 'boston university experiences',
    37.1: 'boston unviersity theatre',
    29: 'the catsle',
    51: 'dewolfe boathouse',
    18.1: 'gotlieb archibal research center',
    23: 'photonics center'
    }

#dictionary for lots and their areas
garage_area = dict(zip(data.Lot, data.Area))

#dictionary for lot and lot name
lot_name = dict(zip(data.Lot, data.Name))

#dictionary for lot and address
lot_address = dict(zip(data.Lot, data.Address))




class TestGarage(unittest.TestCase):
    
    def test_getArea(self):
        garage = Garage()
        self.assertEqual(garage.get_area(buildings, "school of law"), 4, "The area is wrong")
    
    def test_getName(self):
        garage = Garage()
        self.assertEqual(garage.get_name(lot_name, "Lot H"), "Upper Bridge Lot", "The name is wrong")
        
    def test_getAddress(self):
        garage = Garage()
        self.assertEqual(garage.get_address(lot_address, "Lot H"), "1 University Rd", "The address is wrong")


if __name__ == '__main__':
    unittest.main()

'''
    def test_getGarages(self):
        garage = Garage()
        self.assertEqual(garage.get_garages(garage_area), ['Lot G', 'Lot H', 'Lot Q', 'Lot R'], "The lots are wrong")
'''    
