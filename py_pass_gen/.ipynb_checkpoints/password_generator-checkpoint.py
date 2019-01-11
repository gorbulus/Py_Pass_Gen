'''********************Python Password Generator!!!****************************
===============================================================================
Author: William Ponton
Date: 1.9.19

Description: This build will be a more cleverly written version of my previous Python Password Generator.  I will employ a more elegant solution to the Goals below:

======Goals:======
1. Automatically create the file to store the passwords.
2. Continue creating passwords until the user chooses to exit.
3. Provide a unique combination of upper chars, lower case chars, and special chars.
4. User entered password name and length.
'''

# Import modules
import random
import passwordList as pl

# Console Output

# Welcome and Info
def welcomeMessage():
    return print("\n\n\n Welcome to PyPass Password Generator!!! " + 
          "\nA file will be created for your passwords in your " +
          "Python directory (where you store your Python Scripts.\n")

# Main Menu
def password_menu():
  return print("============================" +
        "======PASSWORD TIME=========" +
        "============================\n\n")  

# Try Again
def try_again(engage):
  print("\n\nPRESS 1 TO MAKE ANOTHER PASSWORD.\n" +
               "PRESS 0 TO EXIT THE PROGRAM.\n")
        return engage = int(input())
                
# Exit Greeting
def exit_message():
  print("=============================================\n" +
        "~Thank you for using the Password Generator!~\n" +
        "=============================================\n")

# Password Display (Console)
def password_output(title, password):
  print("\n=============================================")
  
  
 
  print("=============================================\n")
  print("\n\nTitle: {}".format(title))
  print("\nPassword: {}".format(password))
  print("=============================================\n")


# File Operations
# File Output - enclose in an exception
def file_welcome_message():
    passFile = "myPasswords.txt"
    passFile = open(passFile, "w")
    passFile.write("\n=====WELCOME TO THE PYTHON PASSWORD GENERATOR!!!!!=======\n\n" +
                   "=========================================================\n" +
                   "=====================PASSWORD TIME=======================\n" +
                   "================P=A=S=S=W=O=R=D===T=I=M=E================\n" +
                   "=========================================================\n\n\n")

#Write data to text file
def file_write_password(passFile, title, password):
    return passFile.write(title + "\n" + password + "\n\n")

# Main Program Here
def main():
    engage = 1

    while engage == 1:
      password = ""
      passfile = ""
      passwordList = ""
      passmax = None

      
    for n in range(passmax):
        
           
      password = ""
      try_again(engage)
    else:
      if(engage != 1):
          exit_message()
    passFile.close()
    return 0

       '''Control Initiating Event'''
if __name__ == "__main__":
  main()

