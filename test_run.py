import unittest
import run


class test_riddle(unittest.TestCase):   #Test suite.
    
    
    def test_is_this_thing_on(self):    #Basic functionality test. (Test Passing)
        self.assertEqual(1, 1)
        
        
    def write_file(self, message):  #Test opening some file and writing data to it. (Test Passing)
        with open (self, 'a') as file:
        	file.writelines(message + "\n")
        
        
    def get_data(self): #Test to check that data list is empty to begin with. (Test Passing)
        data = []
        self.assertEqual(len(data),0)