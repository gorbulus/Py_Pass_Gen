'''********************Python Password Generator!!!****************************
===============================================================================
Author: William Ponton
Date: 1.24.19

Description: This build will be a more cleverly written version of my previous Python Password Generator.  I will employ a more elegant solution to the Goals below:

======Goals:======
1. Automatically create the file to store the passwords.
2. Continue creating passwords until the user chooses to exit.
3. Provide a unique combination of upper chars, lower case chars, and special chars.
4. User entered password name and length.
'''
# Constant
DIV_LINE = ("=" * 45)
DIV_LINE_FILE = ("=" * 57)
# Import modules
import random
import py_pass_gen.console_output as co
import py_pass_gen.file_operations as fo
import py_pass_gen.password_list as pl
  
# Main Function
def main():
    # Locals
    engage = 1
    title = ""
    passmax = 0
    password = ""
    passwordList = []
    passFile = "myPasswords.txt"
    passFile = open(passFile, "w")
        
    # Console Output
    welcome_message()
    file_welcome_message(passFile)
        
    while engage == 1:
        co.clear_locals(engage, title, passmax, password, passwordList)
        # User input
        print("\n" + DIV_LINE)
        title = input("\nPassword Title: ")
        passmax = int(input("Password MAX Characters: "))
        # Password List Creation
        pl.passList(passwordList)
        # Password Creation
        pl.password = create_password(passmax, password, passwordList)
        # Password Console Output
        co.password_output(title, password)
        # Password File Output
        fo.file_write_password(passFile, title, password)
        # Repeat or Exit
        engage = try_again(engage)
    # Exit path
    else:
        if(engage != 1):
            # Exit Greeting
            exit_message()
    # Close mypasswords.txt
    passFile.close()
    return 0

# Control Initiating Event
if __name__ == "__main__":
  main()