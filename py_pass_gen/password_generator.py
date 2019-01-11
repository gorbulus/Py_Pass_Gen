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
import console_output as co
import file_operations as fo
import password_list as pl


# Main Function
def main():
    
    engage = 1
    
        # Locals
        password = ""
        passFile = ""
        passwordList = []
        passmax = 0
        
        # Console Output
        co.welcome_message()
        fo.file_welcome_message()
        
    while engage = 1:
        
        # User input
        print("\n=============================================")
        title = input("\nPassword Title: ")
        passmax = int(input("Password MAX Characters: "))
        
        # Password Loop
        for n in range(passmax):
            # Password Creation
            pl.passList(passwordList)
            pl.create_password(passmax, password, passwordList)
            co.password_output(title, password)
            fo.file_write_password(title, password)
            co.try_again()
        else:
            if(engage != 1):
                # Exit Greeting
                co.exit_message()
    passFile.close()
    return 0

# Control Initiating Event
if __name__ == "__main__":
  main()