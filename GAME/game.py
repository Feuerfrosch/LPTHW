from sys import argv

script, Weapon, Armor, Skill, Spell, Jewlery = argv


print "Welcome to:", script
print "Your weapon is a:", Weapon
print "Your armor is a:", Armor
print "Your special skill is:", Skill
print "Your first spell is:", Spell
print "You are also wearing a:", Jewlery

Room0 = raw_input("You are in an empty room with four doors on four walls, \nWhere do you go?>")
print "You walk through the %sern door." % (Room0)
Room1 = raw_input("An armed goblin awaits, what do you do?>")
print "You %s, the goblin is injured. \nHe counterattacks and damages your %s." % (Room1, Armor)
Room11 = raw_input("Suddenly, the goblin runs for his life, you hear a rumbling. What do you do?>")
print "You try to %s, but before you manage to act, \nan earthworm breaks through the floor and eats you alive." % (Room11)
Sorry = raw_input("How do you feel?>")

print "Well don't feel %s, because your %s unleashes its holy power and transforms you into an invincible demigod. \nYou win the game! Woo..congrats...you had like no real choices. Have a great day eh?" % (Sorry, Jewlery)
