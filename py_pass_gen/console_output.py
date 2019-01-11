# Console Output =====================================

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
    
# Password Display (Console)
def password_output(title, password):
  return print("\n=============================================" +
               "\nTitle: {}".format(title) +
               "\nPassword: {}".format(password) +
               "\n=============================================\n")

# Try Again
def try_again(engage):
  print("\n\nPRESS 1 TO MAKE ANOTHER PASSWORD.\n" +
               "PRESS 0 TO EXIT THE PROGRAM.\n")
  engage = int(input())
  return engage
                
# Exit Greeting
def exit_message():
  print("=============================================\n" +
        "~Thank you for using the Password Generator!~\n" +
        "=============================================\n")

