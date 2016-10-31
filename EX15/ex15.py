# imports the argv command to use in this program
from sys import argv

# sets the variables for argv
script, filename = argv

# opens the txt file upon starting the program
txt = open(filename)

# prints a sentence including the name of the file
print "Here's your file %r:" % filename
# prints the content of said file
print txt.read()

# prints a sentence of instruction
print "Type the filename again:"
# allows the user to input the name of the file, which is then put into the variable "file_again"
file_again = raw_input("> ")

# opens the file that was put into raw input
txt_again = open (file_again)

# prints the contents of the file
print txt_again.read()

txt.close()
txt_again.close()
