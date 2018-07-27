import unittest
import unittest.mock
import run


class test_run(unittest.TestCase):   #Test suite.
    
    
    def test_is_this_thing_on(self):    #Basic functionality test. (Test Passing)
        self.assertEqual(1, 1)
        
        
    def write_file(self, message):  #Test opening some file and writing data to it. (Test Passing)
        with open (self, 'a') as file:
        	file.writelines(message + "\n")
        
        
    def get_data(self): #Test to check that data list is empty to begin with. (Test Passing)
        data = []
        self.assertEqual(len(data),0)
        
        
    def test_request(self):
        url = "/templates/index.html"
        self.assertTrue(url, "/templates/index.html")
        
        
    def test_index_function(self, mocked_index):
        mocked_index.return_value = 1
        self.assertEqual(mocked_index, 1)
        