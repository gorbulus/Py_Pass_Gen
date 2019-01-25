# Console Output =====================================

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