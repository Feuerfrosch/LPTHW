from sys import exit
candle = False
crowbar = False
gun = False
score = 0
insanity = 100
lights = False

def cellar_two(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "You encounter the cause of all the rumors surrounding this house."
    print "The Shoggoth, a slimy creature of unspeakable doom, faces you."
    print "Despite your previous encounters with the Mythos, you tremble in fear and slight madness.\nYou lose a fair amount of your already fragile sanity."
    insanity -= 25
    while insanity == 0:
        dead("You go insane and have no control over Dr. Armitage anymore.", score, insanity)

    print "What do you do?"
    choice = raw_input("> ")
    if (("shoot" in choice) or ("revolver" in choice) or ("gun" in choice)) and (gun == True):
        print "The bullet pierces the Shoggoth's gelatenous body. It doesn't seem to be impressed"
        dead("The Shoggoth encases you. You suffocate and die.", score, insanity)
    elif("crowbar" in choice) and (crowbar == True):
        print "The crowbar proves quite effective! You smash the Shoggoth's gelatenous body to pieces!!"
        score += 25
        print "Congratulations! You have bested all odds and disposed of the ill-meaning creature!"
        print "Dr. Armitage can now safely return to Miscatonic University and tell his colleagues about his glorious defeat of the Shoggoth!"
        print "Your score is: %d out of 100." % score
        print "Your remaining sanity is: %d out of 100." % insanity
        exit(0)
    elif ("run" in choice) or ("flee" in choice):
        print "You do not manage to get away."
        dead("The Shoggoth encases you in its gelatenous body. You suffocate and die.", score, insanity)
    else:
        print "You do not manage to %r." % choice
        dead("The Shoggoth encases you in its gelatenous body. You suffocate and die.", score, insanity)



def cellar_one(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    if candle == False:
        print "It is too dark to see anything! You need a source of light."
        print "Do you want to proceed anyway?"
        suicide = raw_input("> ")

        if suicide == "yes":
            dead("You fall down the stairs. You are dead.", score, insanity)
        else:
            print "You got lucky this time..."
            start(candle, crowbar, gun, score, insanity, lights)

    else:
        print "As you walk down the stairs, you see a barren cellar.\nThe wall to your right, weirdly enough, is made of wood!"
        print "You can feel a draft coming from that wall.\nYou can make out a faint sound.\nWhat will you do?"
        choice = raw_input("> ")

        if (("crowbar" in choice) or ("break" in choice)) and (crowbar == True):
            print "You destroy the interior wall and walk into the other part of the cellar."
            cellar_two(candle, crowbar, gun, score, insanity, lights)
        elif ("back" in choice) or ("up" in choice):
            start(candle, crowbar, gun, score, insanity, lights)
        elif ("listen" in choice) or ("hear" in choice):
            print "You hear a sort of slobbering from behind the wooden wall."
            cellar_one(candle, crowbar, gun, score, insanity, lights)
        else:
            print "I don't know what that means."
            cellar_one(candle, crowbar, gun, score, insanity, lights)



def parents_room(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "This seems to be the parent's room."
    print "You see a cross above the queen-sized bed and the Holy Bible on the nightstand."

    if candle == False:
        print "What do you do?"
        choicee = raw_input("> ")
        print "It doesn't seem to make sense to %r here." % choicee
        print "Actually, there doesn't seem to be anything of interest here..."
        print "What do you do now?"

        back = raw_input("> ")
        if "back" in back:
            first_floor(candle, crowbar, gun, score, insanity, lights)
        else:
            print "I don't know what that means."
            parents_room(candle, crowbar, gun, score, insanity, lights)

    else:
        print "A masculine shadow jumps out of the large, wooden closet beside you."
        print "He is wearing a ski mask and wields a machete"
        print "What do you do?"
        choice = raw_input("> ")
        if (("shoot" in choice) or ("gun" in choice) or ("revolver" in choice) or ("attack" in choice)) and (gun == True):
            print "You shoot the burglar, he dies with a scream of intense pain."
            print "You just killed someone. You break down and shudder nervously. You lose some sanity."
            insanity -= 25
            while insanity == 0:
                dead("You go insane and have no control over Dr. Armitage anymore.", score, insanity)

            print "What do you do?"
            go_back = raw_input("> ")
            if "back" in go_back:
                first_floor(candle, crowbar, gun, score, insanity, lights)
            else:
                print "You don't feel like %r right now, you decide to leave the cruel scene behind and go back to the hallway." % go_back
                first_floor(candle, crowbar, gun, score, insanity, lights)

        elif ("run" in choice) or ("flee" in choice):
            print "You manage to escape the burglar.", first_floor(candle, crowbar, gun, score, insanity, lights)
        else:
            print "You have nothing to protect youself with. You are brutally murdered by the burglar."
            dead("Now, you are but a heap of flesh.", score, insanity)



def child_room(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "You are in a children's room. Dolls and stuffed animals are thrown all over the place."
    print "There is a warm and cozy bed by a small, cold fireplace."
    print "As you look around, you notice a lit candle on the nightstand."

    while True:
        print "What will you do?"
        choice = raw_input("> ")

        if ("candle" in choice) or ("take" in choice):
            print "You pick up the candle. You feel a little warmer and safer inside."
            candle = True
            score += 25
        elif ("bed" in choice) or ("lie" in choice) or ("sleep" in choice):
            print "You lie down on the child's bed for a second. You fall asleep from the stress you are in."
            dead("While you sleep, you are eaten by the Shoggoth.", score, insanity)
        elif "back" in choice:
            first_floor(candle, crowbar, gun, score, insanity, lights)
        else:
            print "I don't know what that means."




def first_floor(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "You are on the first floor.\nThere are two doors, the first and the second door."
    print "What will you do?"
    choice = raw_input("> ")

    if "first" in choice:
        child_room(candle, crowbar, gun, score, insanity, lights)
    elif "second" in choice:
        parents_room(candle, crowbar, gun, score, insanity, lights)
    elif ("down" in choice) or ("back" in choice):
        start(candle, crowbar, gun, score, insanity, lights)
    else:
        print "You can't go that way!", first_floor(candle, crowbar, gun, score, insanity, lights)




def living_room(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "In the living room, you immediately notice the foul stench of blood."

    while lights == False:

        print "The lights are turned off.\nWhat do you do?"
        light_choice = raw_input("> ")

        if  ("lights" in light_choice) or ("turn" in light_choice):
            print "You see the dead bodies of the family who lived here.\nThe father seems to have killed his wife and three children."
            print "Then he shot himself in the head with a revolver."
            print "You are horrified and lose some sanity."
            insanity -= 25
            lights = True
            while insanity == 0:
                dead("You go insane and have no control over Dr. Armitage anymore.", score, insanity)
        else:
            dead("You fall over a dead body and break your neck", score, insanity)

    while lights == True:
        print "You are in the lit living room, What do you do?"
        choice = raw_input("> ")

        if ("revolver" in choice) or ("take" in choice):
            print "You pick up the revolver. There are two bullets in the barrel."
            gun = True
            score += 25
        elif ("back" in choice) or ("left" in choice):
            start(candle, crowbar, gun, score, insanity, lights)
        else:
            print "I don't know what that means."
            living_room(candle, crowbar, gun, score, insanity, lights)



def kitchen(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "You are in a small kitchen with a rural vibe."
    print "There is a large wood-stove in front of you."
    print "When you come closer, you notice that a cauldron filled with meat sits on top of it."
    print "Someone seems to have used a crowbar to stir the stew."

    while True:
        print "What will you do?"
        choice = raw_input("> ")

        if ("crowbar" in choice) or ("take" in choice):
            print "You pick up the crowbar."
            crowbar = True
            score += 25
        elif ("stew" in choice) or ("eat" in choice) or ("stir" in choice):
            print "You investigate the stew and realize that it is made of human flesh!"
            print "You throw up and lose some sanity."
            insanity -= 25
            while insanity <= 0:
                dead("You go insane and have no control over Dr. Armitage anymore.", score, insanity)
        elif ("back" in choice) or ("right" in choice):
            start(candle, crowbar, gun, score, insanity, lights)
        else:
            "I don't know what that means."




def dead(why, score_status, sanity_status):
    print why, "YOU LOSE!"
    print "Your score is:",score_status
    print "Your sanity level is:",sanity_status
    exit(0)



def start(candle_status, crowbar_status, gun_status, score_status, insanity_status, lights_status):
    candle = candle_status
    crowbar = crowbar_status
    gun = gun_status
    score = score_status
    insanity = insanity_status
    lights = lights_status

    print "You are playing Dr. Henry Armitage, the head librarian of Miscatonic University, Arkham."
    print "Recently, a small cottage near the town of Kingsport has been rumored to be haunted."
    print "Because you fancied the occult and mysterious vibe of this rumor,\nyou decided to investigate the cottage."
    print "Right now, you are standing in the dark hallway of the cottage.\nNo signs of the family who lived here."
    print "There are doors to the left and to the right, one more at the end of the hallway and lastly,\na stairway to the first floor."
    print "Where do you go?"

    choice = raw_input("> ")
    if "left" in choice:
        kitchen(candle, crowbar, gun, score, insanity, lights)
    elif "right" in choice:
        living_room(candle, crowbar, gun, score, insanity, lights)
    elif ("up" in choice) or ("stairway" in choice):
        first_floor(candle, crowbar, gun, score, insanity, lights)
    elif ("forward" in choice) or ("hallway" in choice) or ("down" in choice) :
        cellar_one(candle, crowbar, gun, score, insanity, lights)
    else:
        print "You can't go that way!", start(candle, crowbar, gun, score, insanity, lights)


start(candle, crowbar, gun, score, insanity, lights)
