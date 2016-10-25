# defines "x", includes the number 10 through the formatter %d
x = "There are %d types of people." % 10
# defines binary
binary = "binary"
# defines do_not
do_not = "don't"
# defines "y", includes the definition of the other two variables through the formatter %s
y = "Those who know %s and those who %s." % (binary, do_not)

# prints the strings x and y, including the number and variable-contents
print x
print y

# prints "I said:", the formatter %r takes the string "x" and adds it after "I said:" with single quotes around it
print "I said: %r." % x    # %r is used, because "x" includes a number
# same with "I also said:" and string "y", the single quotes around the formatter %s don't matter apparently
print "I also said: '%s'." % y

# the variable "hilarious" is defined to be false
hilarious = False
# the variable "joke_evaluation" is defined. r% is used as the formatter, because "joke_evaluation" contains a boolean statement
joke_evaluation = "Isn't that joke so funny?! %r"

# the variables are printed, with hilarious taking the place of %r in line 22
print joke_evaluation % hilarious

# the two variables w and e are defined
w = "This is the left side of..."
e = "a string with a right side."

# they are printed after one another, the + sign adds them together
print w + e
