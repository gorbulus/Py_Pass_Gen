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
    return passFile.write("\n=============================================" +
                          "\nTitle: {}".format(title) +
                          "\nPassword: {}".format(password) +
                          "\n=============================================\n")