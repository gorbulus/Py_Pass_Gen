# main.py
# William Ponton
# 1.24.19
# Main file for the py_pass_gen project

# Constants
DIV_LINE = ("=" * 45)

# Import modules
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
    co.welcome_message()
    fo.file_welcome_message(passFile)
        
    while engage == 1:
        co.clear_locals(engage, title, passmax, password, passwordList)
        # User input
        print("\n" + DIV_LINE)
        title = input("\nPassword Title: ")
        passmax = int(input("Password MAX Characters: "))
        # Password List Creation
        pl.passList(passwordList)
        # Password Creation
        password = pl.create_password(passmax, password, passwordList)
        # Password Console Output
        co.password_output(title, password)
        # Password File Output
        fo.file_write_password(passFile, title, password)
        # Repeat or Exit
        engage = co.try_again(engage)
    # Exit path
    else:
        if(engage != 1):
            # Exit Greeting
            co.exit_message()
    # Close mypasswords.txt
    passFile.close()
    return 0

# Control Initiating Event
if __name__ == "__main__":
  main()