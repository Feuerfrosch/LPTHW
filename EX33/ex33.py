i = 0
numbers = []


def while_loop(m, incr):

    while i < m:
        print "At the top i is %d" % i
        numbers.append(i)

        i = i + incr
        print"Numbers now: ", numbers
        print "At the bottom i is %d" % i

while_loop(23, 3)

print "The numbers: "

for num in numbers:
    print num


    # doesnt seem to work...
