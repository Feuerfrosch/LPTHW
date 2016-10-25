tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* %s
\t* %s
\t* %s\n\t* %s
'''

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat % ("Cat food", "Fishies", "Catnip", "Grass")

#while True:
    #for i in ["/","-","|","\\","|"]:
        #print "%s\r" % i,
