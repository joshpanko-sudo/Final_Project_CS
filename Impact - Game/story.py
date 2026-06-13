from dialogue_manager import character_say

Narrator = character_say("--Narrator--")
Narrator.say("""
Narrator: The date is June 5, 2030. You arrive home after a long day of research.|<><>|
Narrator: You open your phone and see a message from the Research Academy of Tai.|<><>|
Narrator: You read the message and realize you have been selected for a warp technology experiment.|<><>|
Narrator: Thus, you pack your items and fall fast asleep.|<><>|
Narrator: The next day, you fly out to the Research Academny Of Tai in first class and you meet with the leader, Jim Kalper.|<><>|
\n
""")

Jim = character_say("--Jim--")
Jim.say("""
Jim: Welcome to the team! We shall start the test tomorrow.
Jim: You should take some rest now..
\n
""")

Narrator.say("""
Narrator: The next day...
\n
""")

Jim.say("""
Jim: Is everything green?
\n
""")

Mike = character_say("--Mike--")
Mike.say("""
Mike: Everything is go!
Mike: Powering up the warp gate!
Mike: Pressure within chamber is rising.
Mike: Pressure is rising above normal limits.
Mike: !!!!OH NOOOOOOOO!!!
""")

Narrator.say("""
Narrator: BOOOOOOOMMMMM!!!!!!!
Narrator: Thus, the antimatter reactor detonated,resulting in a dimension rift.
Narrator: You wake up outside, you look around and see trees. It feels very comforting.
Narrator: Your calm experience is suddenly shaken by the sound of massive feet walking towards you.
Narrator: You see a massive spider robot rushing towards you, its to mounted gun charging ot fire.

""")
Enemy1 = Enemy("Spider Droid", 20)
Player1 = Player("You", 50)
Stun = False
maxhealcooldown = 3
healcooldown = 0

start_battle(Enemy1, Player1,  Stun, maxhealcooldown, healcooldown)

# SP("The next day.....")
# SP("Jim: Everything on?!?!", 0.0625)
# SP("Mike: Red switch on!!", 0.0625)
# SP("Lakrry: Green switch on!!", 0.0625)
# SP("Loon: Black is blinking?????", 0.0625)
# SP("Jim: Shut it down!!!!", 0.0225)
# SP("Lakrry: ITS TO LATE, ITS FULL POWER!!", 0.0625)
# SP("BLASTTTT!!!!!!!!", 0.0625)
# SP("You appear in a strange new word", 0.0625)
# SP("It looks like your world but......", 0.0625)
# SP("Robots are taking over!!!", 0.0625)
# SP("You: There is massive spider robots everywhere", 0.0625)
# SP("A Spider Droid is going to attack you...", 0.0625)
# SP("Helper: Hey there!", 0.0625)
# SP("Helper: You are going to enter your first battle", 0.0625)
# SP("Helper: Your current health is displayed after each attack", 0.0625)
# SP("Helper: Your attacks are displayed in a list", 0.0625)
# print("--------------------------------------------------------------")