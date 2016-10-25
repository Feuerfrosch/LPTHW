name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

# i dont have internet right now, no idea what the conversion rates are
cm_height = height * 6 # ?...
kg_weight = weight / 2.2 # i think

print "Let's talk about %s." % name
print "He's %d inches or %d centimeters tall." % (height, cm_height)
print "He's %d pounds or %d kilograms heavy." % (weight, kg_weight)
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
age, height, weight, age + height + weight)
