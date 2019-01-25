# console_output.py
# William Ponton
# 1.18.19
# Console output for the py_pass_gen project

# Constants
DIV_LINE = ("=" * 45)

# Welcome and Info
def welcome_message():
  return print("\n\n\nWelcome to PyPass Password Generator!!! " + 
               "\nA file will be created for your passwords.\n")

# Main Menu
def password_menu():
  return print( DIV_LINE +
               "======PASSWORD TIME=========" +
               DIV_LINE + "\n\n")  

# Password Display (Console)
def password_output(title, password):
  return print("\n" + DIV_LINE + "\n" +
               "\nTitle: {}".format(title) +
               "\nPassword: {}".format(password) +
               "\n" + DIV_LINE + "\n")

# Try Again
def try_again(engage):
  print("\n\nPRESS 1 TO MAKE ANOTHER PASSWORD.\n" +
        "PRESS 0 TO EXIT THE PROGRAM.\n")
  engage = int(input())
  return engage
                
# Exit Greeting
def exit_message():
  return print("\n" + DIV_LINE + "\n" +
               "~Thank you for using the Password Generator!~\n" +
               DIV_LINE + "\n")

# Clear locals for next use
def clear_locals(engage, title, passmax, password, passwordList):
  engage = 0
  title = ""
  passmax = 0
  password = ""
  passwordList = []