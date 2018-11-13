import unittest
import run
import subprocess


class test_run(unittest.TestCase):


    #Test No.1, to compare two values and return the result. 
    def test_equal(self):
        expected = "test"
        actual = "test"
        self.assertEqual(expected, actual)

    
    #Test No.2, open a text file and write a value to it. 
    def test_write_to_file(self):
        file = "/test_file.txt"
        value = "test"
        with open (file, "w") as f:
            f.writelines(value + "\n")
        v = [row for row in f]
        self.assertEqual(v, f)
        print("test_ran")
        
        
    #Test No.3 (Part-One), to compare that the value retrieved from a text file is as expected. 
    def test_file(self):
        file = "/test_file.txt"
        value = "test"
        with open (file) as f:
            v = [row for row in f]
            self.assertEqual(v, value)
            
    
if __name__ =='__main__':
    unittest.main()
    
    
    
    
    
    