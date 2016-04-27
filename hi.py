import time
itemf=True
items=[]
inventory=[]
users=[]
badges=0
money=500
mode = "unknown"
import random
print ("Something World v.0.21              by Jiale Yu")
print ("If you wanna see the C++ version, which is a lot faster, you can contact Gabriel, or if you want the Javascript version, contact Chun Kang Lu.")
print ("")
print ("_\~ () |\/| [- ~|~ |-| | |\| (_,   \/\/ () /? |_ |) ")
print ("")
print ("")
print ("Welcome! What's your name?")
name = input(">")
#not used yet
if name == "guest session":
    mode = "guest"
elif name not in users:
    users.append(name)
    mode = "newuser"
else:
    mode = "ruser"
begin = "no"
noc=0
commanding = False
while begin == "no":
    print ("Hi " + name + "! Are you ready to begin? Type yes or no, or type credits to type the credits.")
    begin = input(">")
    if begin == "command":
        commanding == True
        break
    if begin == "exit":
        print ("Game aborted. You may now close the window. To play again, please refresh before rerunning.")
        quit()
    if begin == "yes":
        break
    if noc >= 10:
        print ("STOP PRESSING THE BUTTON OK?!?!?!?!?")
        badges=badges+1
    if begin == "no":
        print ("OK, I'll wait!")
        noc=noc+1
    elif begin == "cheat":
        print ("Congratulations, " + name + "! You have completed BDN World 2D! You have earned the DUMB CHEATER badge! (WINNING THE ACTUAL GAME DOES SOMETHING ELSE)")
        badges=badges+1
        mode = "cheater"
        print ("Ka-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------")
        quit()
    if begin == "credits":
        print ("""

Something World, a Jiale.co side project. Work began Feb something 2016. Work is not copyrighted other than the parts from other things which originally were copyrighted.

IDE(s) used, in order of most used: Repl.It, Pythonanywhere, Ideone.

I owe a great thanks to Simon, who gave me the original idea and a bunch of ascii art. Also thanks for the error message idea!

Copyright for Simon contributed areas:

All credits for BDN ascii art goes to me!

""")
    if begin != "yes" and begin != "no" and begin != "cheat" and begin != "command" and begin != "credits":
        print ("""
File "<JCODE>", input, in entering
SelectionError: Invalid Command""")
        print ("")
        begin = "no"
        badges=badges+1
        continue

if commanding == True:
    while True:
        command = input(">")
        if command == "/level":
            ncommand = input("/level>")
            print ("Sorry, /level based ncommand is not yet avalible. To test the bug-laden beta, please email me at jialeyuella@gmail.com")
        elif command == "/edit":
            ncommand = input("/edit")
            if ncommand == "/intf":
                necommand = input("/edit>/intf>")
                if necommand == "/badge":
                    print ("Editing badge count. Using this feature may cause the game to break, so use with caution.")
                    yesr=input("Type yes to confirm you want to edit badge count:")
                    if yesr == "yes":
                        badge = input("New badge count:")
                    else:
                        break
            elif ncommand == "/mode":
                necommand == input("/edit>/mode>")
                mode = input("Type new mode:")
print ("Are you using c9 or another ide that doesn't support end="" sleeping?")
while True:
    ide=input("[y/n]:")
    if ide == 'y':
        break
    else:
        A = """Welcome to Something World.
        
        In battle, you can use the commands 'attack', 'defend', 'run', 'skip', and 'special'. Here's an example:
        
        
        
        
        An a appeared:
        
        a
        
        attack=0
        hp=5
        defence=0
        special=None
        
        Your stats:
        attack=5
        defence=5
        hp=15
        special=None
        
        What do you do?
        >attack
        You attacked. a has 0 hp.
        
        You defeated a! You earned $0."""
        for x in A:
            time.sleep(0.1)
attack=5
origattack=5
defence=5
origdefence=5
hp=15
orighp=15
special="None yet."
level=1
def match(money,gainmoney,attackern,ehp,eattack,edefence,especial,hp,attack,defence,special):
    eallow = True
    time.sleep(0.5)
    print ("Stats:")
    time.sleep(0.5)
    print ("HP: " + str(ehp))
    time.sleep(0.5)
    print ("Attack: " + str(eattack))
    time.sleep(0.5)
    print ("Defence: " + str(edefence))
    time.sleep(0.5)
    print ("Special: " + especial)
    time.sleep(0.5)
    print ("")
    time.sleep(0.5)
    print ("Your stats:")
    time.sleep(0.5)
    print ("HP: " + str(hp))
    time.sleep(0.5)
    print ("Attack: " + str(attack))
    time.sleep(0.5)
    print ("Defence: " + str(defence))
    time.sleep(0.5)
    print ("Special: " + str(special))
    time.sleep(0.5)
    print ("")
    print ("")
    while hp > 0 or ehp > 0:
        Turn = True
        edefend = False
        if Turn == True:
            if hp <= 0:
                time.sleep(1)
                print ("Oh nose! You died. Care to try again?")
                print ("""
                __     __                        _   _              _
                \ \   / /                       | | (_)            | |
                 \ \_/ /    ___    _   _      __| |  _    ___    __| |
                  \   /    / _ \  | | | |    / _` | | |  / _ \  / _` |
                   | |    | (_) | | |_| |   | (_| | | | |  __/ | (_| |  _
                   |_|     \___/   \__,_|    \__,_| |_|  \___|  \__,_| (_)
                """)
                quit()
            else:
                print ("What do you do?")
                while True:
                    action = input(">")
                    if action == "attack":
                        if edefend == False:
                            ehp = ehp-attack
                            time.sleep(0.5)
                            print ("You attacked. " + attackern + " now has " + str(ehp) + "hp.")
                            turn = False
                            break
                        else:
                            print ("Hey! You can't do that. The enemy is defended!")
                            continue
                    elif action == "defence" or action == "defend" or action == "defense":
                        if eattack > defence:
                            time.sleep(0.5)
                            print ("Defence failed.")
                            turn = False
                            break
                        else:
                            time.sleep(0.5)
                            print ("Defended!")
                            eallow = False
                            turn = False
                            break
                    elif action == "special":
                        print ("Under Construction! Please choose something else for now.")
                        continue
                    elif action == "run":
                        print ("Under Construction! I'm so sorry for this not being usable. But try your best and you will (hopefully) win!")
                        turn = False
                        break
                    elif action == "skip":
                        time.sleep(0.25)
                        print ("You skipped your turn.")
                        turn = False
                        break
                    elif action == "":
                        print ("""
File "<JCODE>", input, in attacking
HEY!Error: THATZ A BLANK LINE! THOZEZ R USELESSZ!""")
                    else:
                        print ("""
File "<JCODE>", input, in attacking
SelectionError: Invalid Command""")
        #Opponent's Turn
        number=random.randint(1,2)
        if ehp <= 0:
            money = money + gainmoney
            print (attackern + " was defeated! You won and gained $" + str(gainmoney) + "!")
            print ("You now have $" + str(money))
            break
        if number == 1:
            hp = hp - eattack
            print ("Enemy is thinking...")
            time.sleep(2)
            print ("Enemy attacked! Attack is " + str(eattack) +". You have " + str(hp) + " left!")
        elif number == 2:
            if edefence >= attack:
                edefend = True
                print ("Enemy is thinking...")
                time.sleep(2)
                print ("Enemy defended themselves! You cannot attack in your next turn!")
            elif edefence < attack:
                print ("Enemy is thinking...")
                time.sleep(2)
                print ("Enemy attempted defending and failed! Enemy did nothing.")
        Turn = True
time.sleep(2.5)
print ("Game started.")
time.sleep(1)
print ("Player is " + name)
print ("if you would like a custom nickname, type y. If not, type n.")
loop = True
while loop == True:
    yesorno=input(">")
    if yesorno == "y":
        print ("OK, what would you like me to call you?")
        name = input(">")
        print ("OK then! " + name + " it is!")
        time.sleep(1)
        loop = False
    elif yesorno == "n":
        print ("Sure! Moving on...")
        loop = False
    else:
        print ("")
time.sleep(1.5)
print ("Battle scene controls: attack, defence, special, run, skip")
time.sleep(1)
time.sleep(1)
print ("")
print ("")
print ("")
time.sleep(2)
print ("----------------------------------------------------------")
time.sleep(1)
print ("You are a kid named " + name + ". One day you decided to walk around in the city.")
time.sleep(1)
print ("CITY: LEVEL 1, EASY")
time.sleep(1)
print ("You meet Mario!")
print ("""
______██████████████       "MY GAME IS TOO BORING! TIME TO RUIN SOMEONE ELSE'S GAME!"
-____██▓▓▓▓▓▓▓▓▓ M ▓████             "Actually, you are making the game more INTRESTING."

-__██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██            "OH. WATEVA"
-__██████░░░░██░░██████
██░░░░████░░██░░░░░░░░██
██░░░░████░░░░██░░░░░░██
-__████░░░░░░██████████
-__██░░░░░░░░░░░░░██
_____██░░░░░░░░░██
-______██░░░░░░██
-____██▓▓████▓▓▓█
-_██▓▓▓▓▓▓████▓▓█
██▓▓▓▓▓▓███░░███░
-__██░░░░░░███████
-____██░░░░███████
-______██████████
-_____██▓▓▓▓▓▓▓▓▓██
-_____█████████████""")
attackern="Mario"
eattack=5
edefence=0
ehp=10
especial="None yet."
gainmoney=100
match(money,gainmoney,attackern,ehp,eattack,edefence,especial,hp,attack,defence,special)
print ("")
print ("")
print ("")
print ("")
print ("")
time.sleep(1.5)
print ("Hi! My name is GBot! You make know me from Simon's drawings. If you know me and my slightly unhelpful personality, don't worry, because my creator gave me some software improvements, and now I am as helpful as a thing programmed by a 11-year old can be! *I wonder if that sounds helpful...")
time.sleep(1)
print ("Anyway, I will tell you about stuff when I feel you need help. Or, you can talk to me by typing GBot in the NexT MenU.")
print ("For GBot to work, it must be installed on your system. Would you like to install now?")
while True:
    ha = input("</G>")
    if ha == "yep" or ha == "yes":
        print ("Nice! Wait a few seconds...")
        time.sleep(5)
        print ("GBot has been installed!")
        break
    else:
        print ("""
File "<JCODE>", input, in attacking
GBotIsAnnoyingError: Sorry, I don't seem to understand. Please type either yes to install or yep to install.""")
        print ("")
time.sleep(0.5)
print ("Thanks for installing me! I hope we get along well. You can request a feature or a bugfix at my creator's email: jialeyuella@gmail.com. Enough, lets move on.")
time.sleep(2)
def nextmenu(items,itemf):
    while True:
        print ("""







































        """)
        print ("NexT MenU: Please choose a choice:")
        time.sleep(0.5)
        print ("*continue*")
        print ("*Battleground* Coming Soon")
        print ("*Go Home* Unlocks at Level 5")
        print ("*Items*")
        print ("*Collection*")
        print ("*Stats*")
        print ("*GBot*")
        option = input(">>")
        if option == "Continue Trip" or option == "continue" or option == "continue trip":
            print ("""


































            """)
            break
        elif option == "items" or option == "Items":
            print ("""

































            """)
            print ("ITEMS:")
            print ("""




            """)
            RefillHealth="HealthMax: refills your health to max"
            AttackDouble="SupaAttack: doubles your attack"
            DefenceDouble="SupaDefender: doubles your defence"
            if itemf == True:
                print ("GBot: Welcome to the items menu! Here you can see your items and use them!")
                print ("GBot: I've added some starter items for you.")
                print ("""





                """)
                items.append(RefillHealth)
                items.append(AttackDouble)
                items.append(DefenceDouble)
            lengthi=len(items)
            lindex=0
            for i in range (lengthi):
                time.sleep(0.5)
                print (items[lindex])
                lindex=lindex+1
            itemf=False
            choicei=input("Items>")
            if choicei == "HealthMax":
                hp = orighp
                print ("Your health is now up to max:" + str(hp))
                time.sleep(1)
        elif option == "stats" or option == "Stats":
            print ("""







































            """)
        else:
            print ("""
File "<JCODE>", input, in attacking
MenuError: Menu could not read your command.""")
nextmenu(items,itemf)
print ("You come to a fork in the road.")
time.sleep(0.5)
time.sleep(0.5)
print ("What do you do?")
wd=input(">")
if wd == "l" or wd == "r" or wd == "left" or wd == "right":
    print ("Oops there is only one path")
elif wd == "forward" or wd == "f":
    print ("There's a fork in the road! Learn to read!")
elif wd == "get fork":
    print ("You removed the fork and put it into your inventory.")
    time.sleep(1)
    inventory.append("Fork: seems to do nothing. Maybe good for stabbing people? NoT that I say that's a good idea...")
print ("Having taken care of the fork in the road, you decide to be bored. You soon realize being bored is very boring. Oh and also, you realise that it is getting dark, and that it might be a good idea to find a place to sleep.")
time.sleep(1)
print ("Whenever you are told that it might be a good idea to sleep, you can type sleep now, and your person will find a place to sleep. Unfortunately your person has bad judgement, so if a bed of nails is nearer than a soft, nice bed, he/she will choose the bed of nails.")
time.sleep(2.5)
print ("You are at a fork in the road again. This time though, it's the kind of fork that looks like this:")
time.sleep(1)
print ("""
  \ \ | | / /
   \ \| |/ /
    \     /
     | | |
     |_|_|    """)
print ("Type anything to continue")
read=input(">")
time.sleep(1)
print ("There are three paths: ONE------------------------------------------------------------")
time.sleep(1)
print ("You hear in the distance: THAT's topytighted you ididots you freeziong idiozt garbageonthestreet!d;l")
time.sleep(1.5)
print ("Anytay,doingpoiseaoshso9s8nfjdopooooooooooooooooooingspriopojgjdsgBDNBDNBDNBDNBDNDBNletzfightdabdn ow that hurt NOTGHT")
print ("Type anything to continue")
stuf=input(">")
time.sleep(1.5)
print ("")
print ("Err...")
time.sleep(1)
print ("Well...")
time.sleep(1)
print ("Um...")
time.sleep(1)
print ("")
time.sleep(1)
print ("""
File "<Sanity>", storyboard, in fork2, ?
RealisticError: Something happened, and we couldn't make sure the game is working properly. You can type exit to continue and disable the workingCheCK.""")
print ("01000001 01101110 00100000 01110101 01101110 01101011 01101110 01101111 01110111 01101110 00100000 01100101 01110010 01110010 01101111 01110010 00100000 01101111 01100011 01100011 01110101 01110010 01110010 01100101 01100100 00101110")
print ("Type anything if your now bored.")
s=input(">")
time.sleep(2)
print ("I'm now bored.")
time.sleep(1)
print ("""


















































""")
print ("There are three paths: 1 leads to a house, 2 leads to a bed of nails with a health drink nearby, 3 leads to---What? Nothing?!?!?!")
print ("Type anything! JUST DO IT")
stuff=input(">")
print ("""











































































































































































































































































































""")
print ("YoU FeEl YoUrEsElF gEtTiNg PuShEd InTo PaTh ThReE!?!?!?!")
print ("AhHhHhHhHhHhHhHhHhHhHHHHhhhhh h hh     hhh  h    h???")
print ("Type anything if your ok with that.")
st=input(">")
print ("""
















































































































""")

time.sleep(2)
''' Again, same here :( '''
print ("")
print ("'Is that a BDN?' you find yourself saying.")
time.sleep(1)
print ("'I'm sooooo a BDN!!!' replies the um... well... kinda-BDN")
time.sleep(1)
print ("You feel that you suddenly know that BDNs can't talk. Well at least not in english. Not that you didn't know that already...")
time.sleep(1)
print ("You find yourself yelling 'Hey! BDNs can't talk! WTF!!!'")
time.sleep(1)
print ("The kinda-BDN replies 'Well, I am a BDN, Jiale.co allowed me to test their BDN speaker. It enables you to ----- KA------------------------------------------------------------------------------------------------------------------")
time.sleep(1)
print ("...")
time.sleep(1)
print ("You hear 'Ka------------------------------------------------------------------------------------------'")
time.sleep(1)
print ("""























































""")
time.sleep(1)
print ("GHhHhhHhHHHHAahahHhhHHHhAHHAHSAHDHAHSHhAHHASIHhoLH is a sound that fills the air.")
print ("")
time.sleep(1)
print ("The BDN attacks you!")
time.sleep(1)
attackern="BDN"
eattack=10
edefence=-1
ehp=35
especial="KA----------------------------"
gainmoney=100
print ("You feel a magical power indulge you.")
time.sleep(1)
print ("You momentarily vanish from the dimention.")
print ("""




















































































               +--------+  +---------------------------------------------------+
               | +------+  |                                                   |
               | +------+  |                                                   |
               |        |  |                                                   |
           +----------------------------------------+                          |
           |   +--------+  |                        |                          |
           |               |                        |                          |
           |               |            +---------------+                      |
           |               |      +-----|-----------|---|----------------------|----+
           |     +---------|------|-----|-----------|--+|                      |    |
           |     +---------+------------|-----------|---|----------------------+    |
    +----------------------------+|     |           |   |                           |
    |      |       +-------------||-----|---+       |   |                           |
    |      |       |             ||     |   |       |   |                           |
    |      |     +--------+      ||     |   |       |   |                           |
    |      +-----|--------|------|------|-----------+   |                           |
    +------------|--------|------+|-+   |   |           |                           |
                 | |      |       |  +--|---------------|------------------------+  |
                 | +------|-------|--|--|---+           |                        |  |
                 |        |       |  |  |               |                        |  |
                 |        |       +--+--|---------------|------------------------+--+
                 +--------+             +---------------+----------------+





Your defence is now 1000
Your attack is now 10
Your mom is now dead





""")
defence=1000
attack=10
mom='dead'
print ("""










""")
gainmoney=500
match(money,gainmoney,attackern,ehp,eattack,edefence,especial,hp,attack)
print ("""













































































""")
print ("Having defeated the BDN, you are satisfied.")
time.sleep(1)
print ("ACK! You feel the extra power you gained is starting to stick!")
time.sleep(1)
print ("")
print ("Your attack is now 10!!!")
origattack=10
attack=10
time.sleep(0.5)
print ("")
print ("You move forward. A cool breeze starts to blow.")
time.sleep(1)
