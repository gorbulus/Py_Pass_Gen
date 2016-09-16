'''********************Python Password Generator!!!****************************
===============================================================================
Author: William Ponton

Date: 9.3.16

Description: This program will be a password generator capable of generating
passwords with different criteria and difficulty.

==================
======Goals:======
==================

1. Generate a complex password with a combination of uppercase and lowercase
characters, numbers, and the symbols "#$%&".

2. Store the passwords in a secure location with a description of each one
and a time to update.

3. Let the user select the complexity and criteria for the password.

===============================================================================
===============================================================================



****VERSION 4 FIXES -
ASKS CHAR LENGTH FOR EACH PASSWORD, MORE CUSTOMIZABLE, FORMATTING
'''
import random

#Welcome line + future menu
print("\n\n\n Welcome to PyPass Password Generator!!! \n")
print("Create a file for your passwords in your Python directory (where you store your Python Scripts.\n")
passFile = input("Filename: \n")
passFile = open(passFile, "w")
passFile.write("=========================================================\n")
passFile.write("=====================PASSWORD TIME=======================\n")
passFile.write("================P=A=S=S=W=O=R=D===T=I=M=E================\n")
passFile.write("=========================================================\n")
passFile.write("=====WELCOME TO THE PYTHON PASSWORD GENERATOR!!!!!=======\n\n\n\n")


print("============================")
print("======PASSWORD TIME=========")
print("============================")
    




#The list of acceptable characters
charListUpper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
charListLower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
intList = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symList = ["#", "$", "%", "&"]

#Variables and counters
password = ""

#passmax = int(input("Enter the maximum number of characters for the password:\n"))
#print("Maximum characters:\n",passmax)



passQuant = int(input("How many passwords would you like to generate?\n"))


for n in range(passQuant):
    
    title = input("Password Title: ")
    passmax = int(input("Enter the maximum number of characters for the password\n"))
    print("Maximum characters:",passmax)
    for n in range(passmax): #Generates one random character per passmax value
        password += random.choice(charListUpper + charListLower + intList + symList) #Adds random characters from the above lists
        
    print("\n\nTitle: ", title + "\nPassword: ", password + "\n\n\n")                
    #print("Password: ", password + "\n\n\n")
    passFile.write(title + "\n")
    passFile.write(password + "\n\n\n")
    password = ""

passFile.close()

    
    
