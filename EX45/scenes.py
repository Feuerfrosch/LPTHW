class Scene(object):

    def enter(self):
        print "This is the parent scene class! And the template enter function."

        exit(1)

class Death(Scene):

    def enter(self):
        print "You have failed your quest to destroy your arch rival and will be forever lost in despair.\nYou lose. "

        exit(1)

class Singapore(Scene):

    def enter(self):
        global sword
        sword = 1
        print "It is the year 1888. You are Grigory, a Russain vampire.\nA brithish cleric named Alaric Carter broke into the den of you and your family while you were out on the hunt in a nearby hamlet."
        print "He slaughtered all except you with his divine strength and now is on the run back to his homeland."
        print "After you mourned your family, you became furious with rage and swore to avenge your dead comrades."
        print "You managed to pick up Alaric's tracks with your superior sense of smell and followed him to Singapore."
        print "He seems to have taken a detour, but for what reason?..."
        print "\n"
        print "You arrive at the port of Singapore.\nWhile passing through the crowded streets, you notice three figures in particular, who, judging by their smell, have come in contact with your enemy."
        # thimblerigger = Huetchenspieler
        print "There is an old thimblerigger, a weapon smith and a conspicuous, strongly tatooed man with a tiger on a leash."


        while True:

            choice = raw_input("> ")
            if "thimblerigger" in choice:
                print "While you approach the old man, he notices you and tells you:"
                print "You must seek the man of god, I can feel it! I could tell you the destination of the ship he boarded."
                print "But I get so lonely and noone trusts my game anymore, why don't you play with me, friend?"
                print "If you win, his destination will also be yours. But if you don't, I will misguide you."
                print "What do you say?"
                print "You agree to his conditions. He shows you the ball, hides it under one of 3 thimbles and rotates them quickly."
                print "Where is the ball now? Under 1, 2 or 3?"
                thimble = "%d" % randint(1,3)
                guess = raw_input("[keypad]> ")

                if guess == thimble:
                    print "He looks under the thimble you pointed at, smiles and says:\nCongratulations, your destiny will be the Indian city of Mumbai."
                    print "You immediately walk back to the port and take a ship to Mumbai."

                    return 'mumbai'

                else:
                    print "He looks under the thimble you pointed at and says:\nYou did well, the man you seek went to the Romanian city of Bucharest."
                    print "You immediately walk back to the port and take a ship to Bucharest."

                    return 'bucharest'

            elif ("weapon" in choice) or ("smith" in choice):
                print "You enter the smith's shop. He looks up and greets you like any other customer."
                print "When you ask him about a british foreigner, he seems to remember Alaric and tells you:"
                print "The guy bought a very high quality sword, the best steel I offer. I have only one more of those in stock."
                print "You decide to buy a chinese sword as well, should it ever come to a confrontation with your now armed enemy."
                print "The blacksmith thanks you for your business and lets you back out onto the streets."

                sword += 1

            elif ("tattoo" in choice) or ("tiger" in choice) or ("conspicuous" in choice):
                print "While getting closer to the man with the tiger, who is toplessly standing by the docks, you notice one of his tattoos."
                print "It looks like a christian cross on his chest."
                print "Upon being confronted about the tattoo and his relationship to Alaric, the man shrieks and unleashes his tiger."
                print "What do you do?"
                tiger = raw_input("> ")
                print "Before you can %s, the tiger comes over you, bites off your head and throws it into the water." % tiger
                print "Although you can't die, your head will forever stay in the murky water of the port."

                return 'death'

            else:
                print "You don't think that is a good idea right now..."

class Mumbai(Scene):

    def enter(self):
        global blessing
        blessing = 1

        print "Upon arriving in the Mumbai area, your sense of smell leads you to a secluded hindu temple in the jungle."
        print "When you enter the great entrance hall, you notice three directions from which Alaric's smell reaches you."
        print "A portal to the right that leads to a lush garden."
        print "A heavy, iron-bound door to the left."
        print "And a staircase in front of you, that leads to a throne of some sort. An old monk is sitting there."
        print "Where do you go?"

        while True:

            direction = raw_input("> ")
            if ("right" in direction) or ("garden" in direction):
                print "In the midst of beautiful flowers, a young scholar sits on a stone platform."
                print "He is deeply emerged in his studies and is initially startled when you approach him."
                print "After discussion who you are looking for, the scholar seems to remember Alaric coming through the temple."
                print "He then says: It wouldnt be fun if you didn't learn anything in the process of finding out, now would it?"
                print "I will pose a question and the answer will tell you where the man went from here."
                print "Say, in what city are the greatest and most culturally advanced emperors of all history buried?"

                while True:

                    descision = raw_input("> ")
                    if descision == "rome":
                        print "The scholar chuckles: A very good answer, a very good answer. Go there and you will surely find men of the church."
                        print "You thank him, exit the temple and decide to leave for Rome the following day."

                        return 'rome'

                    elif descision == "cairo":
                        print "The scholar smiles brightly: You think so too! Very good, very good."
                        print "Go there, and you will find the man of the church."
                        print "You thank him, exit the temple and decide to leave for Cairo the following day."

                        return 'kairo'

                    else:
                        print "That city does not nearly have the honor of holding such great men as the men I mean!"

            elif "left" in direction:
                print "You struggle to move the heavy door, when it opens from the other side and an impressively large man stands in front of you."
                print "He strongly smells of Alaric. You immediately notice a rather fresh wound on his left leg."
                print "After getting him to talk about his wound and from where it stemmed, he introduces himself as a martial artist."
                print "He says that he sparred with the european and that he posesses impressive strength."
                print "The wound on his leg is a remnant of the fight they had."
                print "You try to interrogate him regarding the next destination of your enemy, but the monk does not budge and says:"
                print "He told me that you would come through here and ask about him, and that I am to stop you at all costs."
                print "He and I are friends now, so you have to pay for seeking his death."
                print "\n"
                print "The monk dismantles your limbs with quick, intensely powerful blows."
                print "Then he drags your parts into the deepest cellar of the temple and locks them inside."

                return 'death'

            elif ("up" in direction) or ("forward" in direction) or ("staircase" in direction):
                print "The old monk on top of the throne greets you and introduces himself as head monk of this temple."
                print "You tell him that you have a long journey and a quest ahead of you and you seek help in fulfilling your duty."
                print "The monk asks you: What is it that you truly need to succeed in this life?"
                print "Is it power, which will make people cower before you, so nobody will stand in between you and your goal?"
                print "Is it wealth, which will make your life easy and enjoyable by simply paying everybody around you?"
                print "Or is it fortune, which brings happiness and playful ease into your life?"


                blessings = raw_input("> ")
                if (blessings == "power") or (blessings == "wealth"):
                    print "The monk shakes his head: You are not ready for your journey yet. Please descend and seek help elsewhere."

                elif blessings == "fortune":
                    print "The monk nods: You are ready for your journey. Take this, for it will grant you good fortune always."
                    print "He hands you a divine blessing."
                    print "You walk back down into the main hall."

                    blessing += 1

                else:
                    "I do not know what you speak of."

                    return 'mumbai'

            else:
                print "You don't think that is a good idea right now..."

class Kairo(Scene):

    def enter(self):
        global staff
        staff = 1
        print "You follow your sense of smell to the great pyramids of the pharaos."
        print "Judging by it, Alaric must have gone inside to possibly seek relics."
        print "You decide to enter in his footsteps."
        print "When you arrive in the main hall, the scent dissipates and you are left\nto the descision between 2 doors."

        good_door = "%d" % randint(1,2)
        doors = raw_input("[keypad]> ")
        if doors == good_door:
            print "You enter a room in the midst of which a large stone sarcophagus lies."
            print "Do you look inside?"
            sarc = raw_input("> ")

            if sarc == "yes":
                print "You look inside the sarcophagus, which was suprisingly already opened and smells of Alaric."
                print "You find a staff that is adorned with a carved jackal head on the top."

                staff += 1
                print "Then, you notice that a map of Europe was carved into the stone of the opposing wall."
                print "It seems like the location of an ancient castle in Romania is documented here."
                print "You decide, that Alaric must have been off to that location next, as the wall clearly smells of him."

                return 'bucharest'

            elif sarc == "no":
                print "You decide not to disturb a dead pharao,\nbut you notice that a map of Europe was carved into the stone of the opposing wall."
                print "It seems like the location of an ancient castle in Romania is documented here."
                print "You decide, that Alaric must have been off to that location next, as the wall clearly smells of him."

                return 'bucharest'

            else:
                print "This is a yes or no question. Come on...now you broke the game and have to start over."
                print "Yes, that's right. I am literally punishing you for stupidly answering a yes or no question like this\nby breaking the game at this point. Good Job!"

        else:
            print "You walk into a bare room. There is a pedestal that holds a large book in the middle of the room."
            print "Do you open it?"
            book = raw_input("> ")
            if book == "yes":
                print "You activate a hidden contraption. The door closes and you are forever locked in the grave of the pharaos."

                return 'death'

            else:
                print "You decide to leave the book alone, and because there is clearly nothing here that will help you find Alaric,\nyou decide to just leave the pyramids and give up."
                print "On the way out however, you overhear two locals conversing about a Mr. Carter who just left Egypt for his hometown of London."
                print "You think to yourself: Alaric Carter is back in London. That will be my next destination."

                return 'london'

class Bucharest(Scene):

    def enter(self):
        global blood
        blood = 1
        print "You find the ancient castle not far from the Romanian capital, Bucharest."
        print "You feel at home here, because Romania is not far from Russia and you have always liked castles."
        print "When you enter the main hall, you are in awe of the monumental architecture."
        print "You feel the strong urge to simply sit down, admire the building and grant yourself rest from the long journey."
        print "Do you rest or do you go on?"
        break_time = raw_input("> ")

        if break_time == "rest":
            print "A vampire hunter who was incidentally present, looking for vampires to fight, jumps out from behind a statue."
            print "He uses holy water to detach your spirit from your undead body and banishes your soul to the estate."
            print "Now you can be Dracula's eternal ghost buddy."

            return 'death'
        else:
            print "You go on and eventually find a large bedroom."
            print "A huge tome that holds the smell of Alaric peaks your interest."
            print "Upon skimming it, you notice that Alaric must have looked for a certain information:"
            print "On one of the pages, the tome describes the blade of a mighty warrior, hidden away in a church."
            print "The next page, which would have held the information regarding the blade's location was ripped out."
            print "\n"
            print "Suddenly, you feel someone breathing down your neck:"
            print "I could tell you about the man who did this to my encyclopedia. And where he will be looking for that blade."
            print "You slowly turn around, just to find yourself face to face with your (literally) immortal idol: Dracula."
            print "He seems annoyed by your nervous giggling and commands you to be silent."
            print "In the unfolding conversation, it becomes apparent that Dracula is very bored\nand would like you to entertain him for the information you seek."
            print "He suggests you show him, that you are indeed a true and worthy vampire."
            print "Your immediate thoughts are: biting him, fighting him or turning into a giant bat."

            power = raw_input("> ")
            if ("fight" in power) or ("fighting" in power):
                print "Dracula defeats you with ease, but he seems a little less bored."
                print '"That was not too bad! I will tell you where the priest has gone.\nThe blade he seeks is hidden away in a temple near Mumbai."'
                print "You thank Dracula and leave, before giving the awesome castle one last look."

                return 'mumbai'

            elif ("bite" in power) or ("biting" in power):
                print "You are so obsessed with the man, the legend that you bite him and drink some of his blood."
                print "You can feel yourself getting stronger with every drop of blood that you ingest."
                print "After you are done, Dracula seems very impressed: Noone has dared to do THAT to me in ages."
                print "You are a fine vampire, I shall tell you that the priest left for Rome."
                print "You thank Dracula and leave, before giving the awesome castle one last look."

                blood += 1

                return 'rome'

            else:
                print "You just decide to turn into a gigantic bat and fly around, showing Dracula your skill."
                print "When you turn back, he seems quite amused and grants you his respect:"
                print '"You are a fine vampire, I shall tell you that the priest left for Rome."'
                print "You thank Dracula and leave, before giving the awesome castle one last look."

                return 'rome'

class Rome(Scene):

    def enter(self):
        global coins
        coins = 1
        print "Upon coming into the city of Rome, you find a little chapel that smells of Alaric."
        print "You walk up to the altar at the back wall."
        print "Two objects here smell especially of your enemy:\nThe silver cross on the wall\nAnd a small wooden box on the altar."
        print "Which one do you inspect further?"


        relic = raw_input("> ")
        if "cross" in relic:
            print "You touch the silver cross and immediately feel your soul being drained from your body and into the cross."

            return 'death'

        else:
            print "You open the wooden box and find 30 silver coins inside."
            print "You deduce that these must be the coins of Judas."
            print "When you here footsteps coming, you quickly close the box and put the coins in your pocket."

            coins += 1

            print "When you turn around, you see an old catholic priest approach you:"
            print "What can I do for you, friend? He asks."
            print "You tell him that you are looking for a british priest who came through here earlier."
            print "He replies: Yes, indeed I know who you speak of and where he was headed to."
            print "He came here to obtain the dagger of Brutus, Ceasar's son."
            print "But before I tell you his current location, please answer this question:\nHave you sinned?"

            sin = raw_input("> ")
            if sin == "yes":
                print "Then, my child, undo these sins by slaying an even greater monster than yourself."
                print "The brit went back to London, to deal with a man named Jack the Rippper."
                print "If you are after the priest, please consider destroying that malcontent as well."
                print "Go with god, my child."

                return 'london'

            else:
                print "I see, well if you are such a divine spirit, then I will surely tell you where he whom you seek went."
                print "The man said that he would visit the great Pyramids next. Go there and you will surely find him."
                print "Go now, my child."

                return 'kairo'

class London(Scene):

    def enter(self):
        global jack
        jack = 1
        print "In his hometown of London, you look for Alaric everywhere, but you cannot seem to ever find him."
        print "While you're walking through the streets of whitechapel, the silhouette of a man jumps out onto the street:"
        print "I am Jack the Ripper! Utter your last words, if you have any."
        print "Will you fight him, or strike up a conversation?"
        choice = raw_input("> ")

        if "fight" in choice:
            print "While you fight him, you notice that he posesses the strength and speed of a vampire."
            print "You are dismantled by his long blade and thrown into the gutter."

            return 'death'

        else:
            print "You somehow mangage to get a conversation started."
            print "You discover that both of you are vampires and that Alaric is your mutual enemy."
            print "Jack tells you that he has inside information about Alaric's next destination."
            print "A source of Jack's overheard a conversation he had, about visiting his familie's graves in Trondheim, Norway."

            jack += 1

            print "\n"
            print "Jack and you find the last ship that is willing to put out to sea tonight."
            print "Unfortunately the captain demands payment, because he has plans to sail elsewhere."
            print "How many Pounds do you give him?"

            pounds = int(raw_input("> "))

            if pounds < 500:
                print "You find yourself back in Singapore, when she ship enters the port."

                return 'singapore'

            else:
                "You find yourself in Trondheim, when the ship enters the port."

                return 'trondheim'

class Trondheim(Scene):

    def enter(self):

        print "You and Jack find Alaric kneeling by a grave on a cliff by the sea."
        print "Alaric slowly turns around and looks you straight in the eye."
        print '"Grigory, Jack. Come to send me to my lord and saviour?"'
        print "You speak up to him: You will pay for what you did to my family!"
        print "You won't go to heaven when I am done with you, you will forever burn in hell!"
        print "He laughs dirtily, then starts to shout as well:"
        print "Do you know how my wife and daughter died? A vampire ate them for lunch."
        print "Just like you eat a cow or a chicken. That is why I will have my revenge."
        print "By destroying every single one of you beasts!"
        print "\n"
        print "With intense rage, he draws a chinese sword and charges at you."

        if (sword > 1) and (blessing > 1) and (staff > 1) and (blood > 1) and (coins > 1) and (jack > 1):
            print "You draw your chinese sword and counter his blow."
            print "A viscious fight ensues. Suddenly, your sword slips out of your hand."
            print "Alaric grins as he goes for the kill, but your devine blessing seems to work:"
            print "His sword misses you by an inch and shatters on a headstone."
            print "He pulls out a staff, adorned with a carved bird's head on top."
            print "You pull out your staff of Anubis and once again,\nyou and your opponent are entangled in a battle to the death."
            print "As the two ancient staffs collide, bursts of light and dark energy are released into the air."
            print "You can feel the blood of Dracula coarsing through your body, and lending you strength."
            print "Eventually, you gain the upper hand and slowly force your opponent back."
            print "The cliff is now only a few meters away, but suddenly, Alaric draws a mighty dagger and stabs you."
            print "Luckily, the coins of judas protect your heart as the dagger slides off of them."
            print "Just then, Jack the Ripper stabs Alaric into the abdomen."
            print "You use the opportunity and deal a blow to his head.\nHe is filled with dark energy and dies with a sigh."
            print "His body looks like it has been decaying for weeks, having all its life energy drained."
            print "\n"
            print "You won, but you feel slightly empty inside. All you worked so hard for lies on the floor before you."
            print "You thank Jack for his help and together you bury the body in the family grave."
            print "You take one more look back, and finally set off for your homeland, in which more death and loneliness awaits you."

            return 'finished'

        else:
            print "You manage to avoid his hate-filled blow.\nA long, heated battle ensues.\nAlthough, Jack and you both fight him at the same, he has intense stamina and strength for a human."
            print "It is almost as if a divine power gave him strength.\nJack is the first to fall, eventually, you are pushed back toward the clif."
            print "With a last strike, Alaric sends you over the edge before collapsing from exhaustion."
            print "In this moment, you realize that you have nothing left to live for anymore."
            print "Even if you had destroyed your enemy, there would have been nothing left except for emptyness."
            print "You embrace your fate. Then you hit the ground. You are impaled by a tree at the bottom of the cliff."
            print "You will be with your family now. You smile as you fade into nothingness."

            return 'death'


class Finished(object):
    def enter(Scene):
        print "Your arch rival has been cast into eternal oblivion and will forever pay for what he did to your kind."

        return 'finished'
