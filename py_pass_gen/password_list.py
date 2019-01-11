
#********************Python Password Generator!!!****************************
#===============================================================================
#Author: William Ponton
#Date: 12.29.18
#
#Description: This module creates four lists:
#              UPPER CASE
#              LOWER CASE
#              INTEGER (0 - 9)
#              SYMBOLS (#, $, %, &)
#  1. The lists are populated by a range of ASCII Integers of their category.
#  2. A second list of random items from each parent list is created.
#     a. This technique provides an even probability of a pick from lists of differing lengths.
#  3. A third Master List is returned of random characters from each of the previous lists (passwordList).

# Import random module
import random

# Lists of acceptable password characters.
#   Each list is populated with the ASCII Integer values that correspond to their category:
#   UPPER CASE (A - Z)
#   LOWER CASE (a - z)
#   INTEGERS   (0 - 9)
#   SYMBOLS    (#, $, %, &)

def passList(passwordList):
  # Upper Case A - Z (ASCII codes 67 - 90)
  charListUpper = list(range(67, 91))
  # Lower Case a - z (ASCII codes 97 - 122)
  charListLower = list(range(97, 123))
  # Integers 0 - 9 (ASCII codes 48 - 57)
  intList = list(range(48, 58))
  # Special Characters: #, $, %, &, :, ? (ASCII codes: 35, 36, 37, 38, 58, 63 )
  symList = list(range(35, 39))
  # Equal Probablility of a pick from each list
  upperPick = random.choice(charListUpper)
  lowerPick = random.choice(charListLower)
  intPick = random.choice(intList)
  symPick = random.choice(symList)
  '''Create a master list of randomized ASCII Characters'''
  passwordList = [upperPick, lowerPick, intPick, symPick]
  return passwordList

# Use the password list to create a password
def create_password(passmax, password, passwordList):
   for n in range(passmax):
    pl.passList(passwordList)
    password += chr(random.choice(passwordList))
    return password
  