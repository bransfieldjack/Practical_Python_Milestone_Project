import os
import random


def add_user_to_file():
    f = open('files/users.txt', 'a')
    name = f.write("jack")
    f.close()
    print(name)
    
    
add_user_to_file()

def add_username(username):
    with open ('files/users.txt', 'a') as file:
        file.writelines(username)
        
