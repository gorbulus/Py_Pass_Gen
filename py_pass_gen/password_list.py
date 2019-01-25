# password_list.py
# William Ponton
# 1.24.19
# Password generating algorithm for the py_pass_gen project

# Import modules
import random

def passList(passwordList):
  # Upper Case A - Z (ASCII codes 67 - 90)
  charListUpper = list(range(67, 91))
  # Lower Case a - z (ASCII codes 97 - 122)
  charListLower = list(range(97, 123))
  # Integers 0 - 9 (ASCII codes 48 - 57)
  intList = list(range(48, 58))
  # Special Characters: #, $, %, & (ASCII codes: 35, 36, 37, 38)
  symList = list(range(35, 39))
  # Equal Probablility of a pick from each list
  # Upper Case
  upperPick = random.choice(charListUpper)
  # Lower Case
  lowerPick = random.choice(charListLower)
  # Integer
  intPick = random.choice(intList)
  # Symbol
  symPick = random.choice(symList)
  # Create a master list of randomized ASCII Characters
  passwordList += [upperPick, lowerPick, intPick, symPick]
  return passwordList

# Use the password list to create a password
def create_password(passmax, password, passwordList):
  for n in range(passmax):
    passList(passwordList)
    password += chr(random.choice(passwordList))
    # print(password)
  return password
