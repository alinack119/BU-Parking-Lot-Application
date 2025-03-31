# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 20:02:39 2022

@author: Alina
"""

import unittest
from spaces import Spaces

class TestSpaces(unittest.TestCase):
    
    def test_getSpaceNumber(self):
        spaces = Spaces("Lot H")
        self.assertEqual(spaces.get_spaceNumber(), 30, "The number is wrong")
    
    def test_enterLot(self):
        spaces = Spaces("Lot H")
        self.assertEqual(spaces.enter_lot(), 29, "The number is wrong")
        
    def test_exitLot(self):
        spaces = Spaces("Lot H")
        self.assertEqual(spaces.exit_lot(), 30, "The number is wrong")
    
    

if __name__ == '__main__':
    unittest.main()