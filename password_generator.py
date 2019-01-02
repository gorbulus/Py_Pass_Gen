'''********************Python Password Generator!!!****************************
===============================================================================
Author: William Ponton
Date: 12.29.18

Description: This build will be a more cleverly written version of my previous Python Password Generator.  I will employ a more elegant solution to the Goals below:

======Goals:======
1. Automatically create the file to store the passwords.
2. Continue creating passwords until the user chooses to exit.
3. Provide a unique combination of upper chars, lower case chars, and special chars.
4. User entered password name and length.
'''

'''Import random module'''
import random

'''Welcome & Info'''
print("\n\n\n Welcome to PyPass Password Generator!!! \n")
print("A file will be created for your passwords in your Python directory (where you store your Python Scripts.\n")

'''Menu & Flow Control Here'''


'''File Operations - enclose in an exception'''
passFile = "myPasswords.txt"
passFile = open(passFile, "w")
passFile.write("\n=====WELCOME TO THE PYTHON PASSWORD GENERATOR!!!!!=======\n\n")
passFile.write("=========================================================\n")
passFile.write("=====================PASSWORD TIME=======================\n")
passFile.write("================P=A=S=S=W=O=R=D===T=I=M=E================\n")
passFile.write("=========================================================\n\n\n")

'''Test to see if file is successful and confirm'''
   

'''Lists of acceptable password characters.
   Each list is populated with the ASCII Integer values that correspond to their category:
   UPPER CASE (A - Z)
   LOWER CASE (a - z)
   INTEGERS   (0 - 9)
   SYMBOLS    (#, $, %, &)
   '''

''' Upper Case A - Z (ASCII codes 67 - 90)'''
charListUpper = list(range(67, 91))

''' Lower Case a - z (ASCII codes 97 - 122)'''
charListLower = list(range(97, 123))

''' Integers 0 - 9 (ASCII codes 48 - 57)'''
intList = list(range(48, 58))

''' Special Characters: #, $, %, &, :, ? (ASCII codes: 35, 36, 37, 38, 58, 63 )'''
symList = list(range(35, 39))

'''Change this menu to enter and exit'''
print("============================")
print("======PASSWORD TIME=========")
print("============================\n\n")


engage = 1

'''Change this to a while True'''
while engage == 1:
  password = ""
  
  print("=============================================")
  title = input("Password Title: ")
  passmax = int(input("Password MAX Characters: "))
  print("\n=============================================\n")
  
  for n in range(passmax):

    '''Equal Probablility of a pick from each list'''
    upperPick = random.choice(charListUpper)
    lowerPick = random.choice(charListLower)
    intPick = random.choice(intList)
    symPick = random.choice(symList)

    passwordList = [upperPick, lowerPick, intPick, symPick]
    password += chr(random.choice(passwordList))
  print("\n=============================================")
  print("Title: {}".format(title))
  print("Password: {}".format(password))
  print("=============================================\n")
  passFile.write(title + "\n" + password + "\n\n")
  password = ""

  '''CONTINUE OR EXIT'''
  print("\n\nPRESS 1 TO MAKE ANOTHER PASSWORD.\n")
  print("PRESS 0 TO EXIT THE PROGRAM.\n")
  engage = int(input())

else:
  if(engage != 1):
      print("=============================================\n")
      print("~Thank you for using the Password Generator!~\n")
      print("=============================================\n")
passFile.close()

    © 2019 GitHub, Inc.
    Terms
    Privacy
    Security
    Status
    Help

    Contact GitHub
    Pricing
    API
    Training
    Blog
    About

