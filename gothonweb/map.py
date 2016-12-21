from random import randint

class Scene(object):
    def __init__(self, title, urlname, description):
        self.title = title
        self.urlname = urlname
        self.description = description
        self.paths = {}

    def go(self, direction):
        default_direction = None
        if '*' in self.paths.keys():
            default_direction = self.paths.get('*')
        return self.paths.get(direction, default_direction)

    def add_paths(self, paths):
        self.paths.update(paths)

# Create the scenes of the game
campaign_choice = Scene("You have the choice!", "campaign_choice", """Choose between humans and gothons!
Just type in human or gothon to get started!""")

help_screen_cptn_obvious = Scene("Captain Obvious is here to save you!", "help_screen_cptn_obvious", """Seriously?
It literally just said "type in human or gothon...do you really need further help with that? Go ahead,
just pick one...type it in down there, please, be my guest. Or don't, because you might not be able to solve this
simple, little game. It's up to you!""")

help_screen_gothon = Scene("Help Screen", "help_screen_gothon", """This is the help screen!
It shows you the possible inputs for this game at its various stages and also lets you jump to any stage you desire.
Possible inputs:
gothon bridge: shoot bomber, refuse, shoot chaser
shooting the chaser: tell her the truth, attack her, lie
lying: live on my onw, relationship
having a relationship: have kids, dont have kids

To jump to one of the scenes, just write their name as done above.
Have a good day!""")

gothon_bridge = Scene("The bridge of the Warleader", "gothon_bridge", """You are M'zarek, a lowly officer on board
of the Warleader, the Gothon's main battleship. A fierce battle between gothons and humans has broken out in the space
around the ship, on which you command one of the two gigantic plasma cannons. Your commanding officer orders you to shoot
the human imperial bomber, because it poses a threat to the Warleader and seems to target this main ship. As you look closer,
you notice that a human woman is piloting the bomber. Although she doesn't belong to your species, you are stunned by her beauty.
Right beside the bomber, a swift imperial chaser battles multiple gothon fighters at once.
Which ship will you shoot, or will you shoot at all?""")

shot_bomber_death = Scene("You shot the bomber", "shot_bomber_death", """You direct your plasma cannon at the bomber containing
the beautiful human female. As you push the trigger button, a bright ray engulfs the vehicle and it explodes into space.
Upon noticing that the bomber has been destroyed, the imperial chaser stops fighting the gothon ships and comes right at the bridge
of the Warleader. Before the chaser bursts through the windows and impales you, you see the tears on the face of the male human pilot.
You die knowing, that your actions have destroyed two people and their young love.""")

refused_death = Scene("You refused to shoot", "refused_death", """You are sick of killing other lifeforms and cannot
bring yourself to do anymore harm to anyone, not even agressive creatures from other planets like the humans.
When your commanding officer notices, that you will not fire the plasma cannon, he falls into an intense rage
and tries to knock you out, so he can fire the cannon instead. You manage to resist him for some time, but
eventually, he overpowers you and you fall to the ground. Unfortunately, the bomber has already come close enough
and your last thought before the Warleader explodes is "I saved a beautiful being from certain death.
I can die happily knowing that.""")

shot_chaser = Scene("You shot the chaser", "shot_chaser", """You can't bring yourself to extinguish such beauteous life and thus
shoot the chaser instead. Your commanding officer scolds you and calls you a fool, as the bomber continues to approach the Warleader.
It almost manages to bomb your ship, but the gothon fighters that fought the chaser before you destroyed it, came after
the bomber and now blast it's engine. It crashes into the upper part of the Warleader and you are swept off your feet and fall unconscious.
When you awake, you hear blaster shots and a fellow gothon's death-scream. Then you open your eyes and see the female
bomber pilot standing above you, ready to kill you. There are corpses with blaster holes all around you.""")

truth_death = Scene("You told her the truth", "truth_death", """You quickly tell her, that you never meant to kill her and that you
shot the imperial chaser instead. Her face displays a look of hurtful surprise, then she tears up. "You killed my
husband then. Die, gothon scum!" She fires 5 blaster rounds into your face and you die.""")

attack_pilot_death = Scene("Attack!", "attack_pilot_death", """You pretend to be fearful, but then you use the special gothon
kung fu you were taught at the academy. You hit her pressure points and she explodes from within. You decide to go on ahead and
see if there are any survivors and a way off the instable ship. When you get to the upper docking station, a cohort of human
soldiers approach you from their recently docked ship and blast you to bits. You die knowing that you extinguished the life
of something beautiful for no greater reason.""")

lie = Scene("You lie to her", "lie", """You quickly tell her, that you couldnt bring yourself to kill any more people.
You say you fought your commanding officer, but he overpowered you and shot the chaser. The female pilot drops her blaster
and breaks out into tears. She tells you, that the chaser's pilot was her husband. After calming down, the beautiful female suggests that you
come with her to earth, if you do not want to kill for the gothons anymore. You are amazed by the invitation and decide to follow her.
The other soldiers are sceptical at first, but after a while on the long flight back to earth, they accept you as one of their own.
When you finally arrive, you ask yourself wether you should try to get into a relationship with the pilot or go live on your own.""")

alone_death = Scene("You try to live alone", "alone_death", """You decide to give her time to get over her husband, whom you killed
(you are pretty evil, dude...). One day, on your way to the grocery store, you are killed by a crowd of gothon-racist humans,
who are still hateful towards the gothons, despite having one the long war in the last, descisive battle.
They carry your head around town on a pitchfork (you deserved that for lying!)""")

relationship = Scene("You try to get into a relationship", "relationship", """You decide that she is too beautiful to resist trying to
get with her (wow, you are really evil, man!). Your constant courting seems to flatter her and after a while, she agrees to go out on a date.
A few years go by and the two of you ask yourself, wether you should try to have kids or just be a couple.""")

legs = {
    1:"tentacles for legs",
    2:"gothon legs",
    3:"human legs",
    4:"spider legs",
    5:"snakes for legs"
}

head = {
    1:"human heads",
    2:"gothon heads",
    3:"cthulian heads",
    4:"robot heads",
    5:"wookie heads"
}

arms = {
    1:"chainsaws for arms",
    2:"tentacles for arms",
    3:"crab pincers",
    4:"sarlac teeth",
    5:"snakes for arms"
}

kids_death = Scene("You decide to have kids", "kids_death", """You two decide, that without having children, you would feel
empty and incomplete together. 9 months later, your beautiful pilot gives birth to a monstrous atrocity, which probably
became so terrible due to gene exchange between a human and a gothon. It has %d %s, %d %s and %d %s, which it uses to
turn both of you into minced meat before going on a rampage on earth. You die knowing that you truly have created
something evil through your vicious deeds You lose (this is the worst ending :O).""" % (randint(2,9), legs.get(randint(1,5)), randint(2,9), head.get(randint(1,5)), randint(2,9), arms.get(randint(1,5)) ))

no_kids_winner = Scene("You decide not to have kids", "no_kids_winner", """You are afraid that breeding in between species could result
in terrible mutations and simply decide to live your life to the fullest. You both die at an old age, having lived happily in a time,
when the war between gothons and humans was quickly forgotten and peace and prosperity ruled over the universe.""")


help_screen_human = Scene("Help Screen", "help_screen_human", """This is the help screen!
It shows you the possible inputs for this game at its various stages and also lets you jump to any stage you desire.
Possible inputs:
Central Corridor: shoot!, dodge!, tell a joke
Laser Weapon Armory: Please enter a three digit numeric code between 1 and 3 here. Good Luck!
The Bridge: throw the bomb, slowly place the bomb
Escape Pod: Please enter a number in between 1 and 5 (including those) here. Good Luck!

To jump to one of the scenes, just write their name as done above.
Have a good day!
""")

central_corridor = Scene("Central Corridor", "central_corridor",
"""
The Gothons of Planet Percal #25 have invaded your ship and destroyed
your entire crew. You are the last surviving member (oh noes!) and your
last mission is to get the neutron destruct bomb from the Weapons Armory,
put it in the bridge, and blow up the ship after getting into an escape pod.

You're now running down the central corridor to the Weapons Armory when a
Gothon hops out in an evil clown costume filled with hate. He's blocking the door
to the Armory and about to pull a weapon to blast you.
""")

laser_weapon_armory = Scene("Laser Weapon Armory", "laser_weapon_armory",
"""
Lucky for you they made you learn Gothon insults in the academy.
You tell the one Gothon joke you know:
Lbhe zbgure vg fb sng, jura fur vfvg nebhaq gut ubhfr, fur fvgf nebhaq gut ubhfr.
The Gothon bursts into laughter and rolls around on the ground. While its
laughing you run up and use your copy of Nietzsche's notebooks (translated into Gothon)
to lecture the Gothon on the shaky foundations of its ideologies. While it tries
to cope with its existential crisis, you leap through the Weapon Armory door.

You dive roll into the Weapon Armory, crouch and scan the room for more Gothons
that might be hiding. It's dead quiet, too quiet.
You stand up and run to the far side of the room and find the neutron bomb in its
container. There's a keypad lock on the box and you need the code to get the bomb
out. If you ultimately get the code wrong then the lock closes forever and you can't
get the bomb. The code is 3 digits between 1 and 3.\n
If you want to give up, simply type in "I give up"
""")

the_bridge = Scene("The Bridge", "the_bridge",
"""
The container clicks open and the seal breaks, letting gas out. You grab the
neutron bomb and run like heck to the bridge where you place it in the right spot.
You burst into the Bridge with the bomb under your arm and surprise 5 Gothons
who are trying to take control of the ship. Each of them has an uglier clown costume
that the last. They don't pull their weapons out of fear that they will set off
the bomb under your arm.
""")
escape_pod = Scene("Escape Pod", "escape_pod",
"""
You gesture towards the bomb and threaten to set it off, the Gothons put up
their arms and ask for a truce. You inch backwards to the door, open it, and
carefully place the bomb on the floor, waving your finger over the detonate button.
Then you jump back through the door, hit the close button and zap the lock so they
can't get out. Now that the bomb is placed you run to the escape pod.
You rush through the ship desperately trying to make it to the escape pod. It seems
like there's no Gothons around, so you run as fast as possible. Eventually you reach
the room with the escape pods, and you now need to pick one to take. Some of them could
be damaged, but you don't have time to look. There's 5 pods, which one do you take?
""")
the_end_winner = Scene("You Made It!", "the_end_winner",
"""
You jump into pod 2 and hit the eject button. The pod flies out into space heading
to the planet below. As you're heading down, you look back and see your ship implode
and then explode like a supernova, taking down the Gothon ship at the same time.
You made it!
""")
the_end_loser = Scene("...", "the_end_loser",
"""
You jump into a random pod and hit the eject button. The pod escapes into space
but there's a crack in the hull. Uh oh. The pod implodes and you with it.
""")
shoot_death = Scene("Death...", "shoot_death", """ Quick on the draw you yank out your blaster and fire it at the Gothon.
His clown costume is flowing and moving around his body, which throws
off your aim. Your laser hits his costume but misses him entirely. The laser
completely ruins his brand new costume his mother bought him, which
makes him fly into an insane rage and blast you repeatedly in the face
you are dead. Then he eats you.
""")
dodge_death = Scene("Death...", "dodge_death", """ Like a world class boxer you dodge, weave, slip and slide right
as the Gothons blaster cranks a laser past your head.
In the middle of your artful dodge your foot slips and you
bang your head on the metal wall and pass out.
You wake up shortly after only to die as the Gothon stomps on
your head and eats you.
""")
code_death = Scene("Death...", "code_death", """ "The lock buzzes one last time and then you hear a sickening
melting sound as the mechanism is fused together.
You decide to sit there, and finally the Gothons blow up the
ship from their ship and you die.
""")

throw_death = Scene("Death...", "throw_death", """ In a panic you throw the bomb at the group of Gothons
and make a leap for the door. Right as you drop it a
Gothon shoots you right in the back killing you.
As you die you see another Gothon frantically try to disarm
the bomb. You die knowing they will probably blow up when
it goes off.
""")

# Define the action commands available in each scene
podcode = '%d' % randint(1,5)
escape_pod.add_paths({
    podcode: the_end_winner,
    '*': the_end_loser,
    'help': help_screen_human
})
the_bridge.add_paths({
    'throw the bomb':  throw_death,
    'slowly place the bomb': escape_pod,
    'help': help_screen_human
})
counter = '%d%d%d' % (randint(1,3), randint(1,3), randint(1,3))
laser_weapon_armory.add_paths({
    counter: the_bridge,
    'I give up': code_death,
    'help': help_screen_human,
    '*': laser_weapon_armory
})
central_corridor.add_paths({
    'shoot!':shoot_death,
    'dodge!':dodge_death,
    'tell a joke': laser_weapon_armory,
    'help': help_screen_human
})
help_screen_human.add_paths({
    'Central Corridor':central_corridor,
    'Laser Weapon Armory':laser_weapon_armory,
    'The Bridge':the_bridge,
    'Escape Pod':escape_pod
})

relationship.add_paths({
    'have kids':kids_death,
    'help':help_screen_gothon,
    'dont have kids':no_kids_winner
})
lie.add_paths({
    'live on my own':alone_death,
    'help':help_screen_gothon,
    'relationship': relationship
})
shot_chaser.add_paths({
    'tell her the truth':truth_death,
    'attack her':attack_pilot_death,
    'lie':lie,
    'help':help_screen_gothon
})
gothon_bridge.add_paths({
    'shoot bomber':shot_bomber_death,
    'refuse':refused_death,
    'shoot chaser':shot_chaser,
    'help':help_screen_gothon
})
help_screen_gothon.add_paths({
    'gothon bridge': gothon_bridge,
    'shooting the chaser': shot_chaser,
    'lying': lie,
    'having a relationship': relationship
})
help_screen_cptn_obvious.add_paths({
    'human': central_corridor,
    'gothon': gothon_bridge

})
campaign_choice.add_paths({
    'human':central_corridor,
    'gothon':gothon_bridge,
    'help':help_screen_cptn_obvious
})

# Make some useful variables to be used in the web application
SCENES = {
    campaign_choice.urlname : campaign_choice,
    help_screen_cptn_obvious.urlname : help_screen_cptn_obvious,

    help_screen_gothon.urlname : help_screen_gothon,
    gothon_bridge.urlname : gothon_bridge,
    shot_bomber_death.urlname : shot_bomber_death,
    refused_death.urlname : refused_death,
    shot_chaser.urlname : shot_chaser,
    truth_death.urlname : truth_death,
    attack_pilot_death.urlname : attack_pilot_death,
    lie.urlname : lie,
    alone_death.urlname : alone_death,
    relationship.urlname : relationship,
    kids_death.urlname : kids_death,
    no_kids_winner.urlname : no_kids_winner,

    help_screen_human.urlname : help_screen_human,
    central_corridor.urlname : central_corridor,
    laser_weapon_armory.urlname : laser_weapon_armory,
    the_bridge.urlname : the_bridge,
    escape_pod.urlname : escape_pod,
    the_end_winner.urlname : the_end_winner,
    the_end_loser.urlname : the_end_loser,
    shoot_death.urlname : shoot_death,
    dodge_death.urlname : dodge_death,
    code_death.urlname : code_death,
    throw_death.urlname : throw_death
}
START = campaign_choice
