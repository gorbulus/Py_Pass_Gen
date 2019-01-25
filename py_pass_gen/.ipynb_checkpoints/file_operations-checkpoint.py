# file_operations.py
# William Ponton
# 1.18.19
# File operations for the py_pass_gen project

# Constants
DIV_LINE_FILE = ("=" * 57)

# File Output - enclose in an exception
def file_welcome_message(passFile):
  return passFile.write("\n=====WELCOME TO THE PYTHON PASSWORD GENERATOR!!!!!=======\n\n" +
                        DIV_LINE_FILE +"\n" + "=====================PASSWORD TIME=======================\n" +
                        "================P=A=S=S=W=O=R=D===T=I=M=E================\n" + DIV_LINE_FILE + "\n\n\n")

#Write data to text file
def file_write_password(passFile, title, password):
  return passFile.write("\n" + DIV_LINE_FILE +
                        "\nTitle: {}".format(title) +
                        "\nPassword: {}".format(password) +
                        "\n"+ DIV_LINE_FILE + "\n")
