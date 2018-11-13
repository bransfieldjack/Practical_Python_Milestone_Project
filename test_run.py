import json


#Non python-unit testing functions:
    
    
#Compare that the value retrieved from a text file is as expected. 
def test_file_2(file, value):
    with open(file) as f:
        f.writelines(value + "\n")
    if value == f:
        print("Test has completed with success. ")
        
        
def test_riddle_file(file, value):
    riddles = []
    with open(file, "r") as riddle_data:
        riddles = json.load(riddle_data)	
                
    if riddles == value:
        print("Test is completing with success. ")
        

test_file_2(file="test_file.txt", value="test")
test_riddle_file(file="test_riddles.json", value="test")