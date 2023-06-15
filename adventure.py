# adventure.py
#? This is a game where you go on an adventure. (Automatic)

### Imports ###
from random import randint
from time import sleep

### Story ###
name = input("What is your name?")
game_over = False
gems_found = 0



print("Long ago, in kingdom Valkyrie, a princess named Ashley has been kidnapped.\nCountless knights tried to save her, but it was useless.\nand It's up to you:", name, ", to save the princess.")

walkway = int(input("Where do you want to go? (1, the Forbidden Forest. 2, the Warping Realm. 3, the Magical lake.)"))
while not game_over:
    if walkway == 1:
        print("Heading to the forbidden forest...")
        sleep(2.5)
        print("You are still on your way, but you see a hostile Woodlander ...")
        print("Eggrie\nAttack: 6\nDefense: 2\nWeapon: None\nSkill: Wood Fist")
        fight = input("Would you like to fight? (Yes/no)")
        if fight == "yes":
            print("FIGHT!")
            sleep(1.5)
            print("Eggrie launched his fist onto you, you lost 20 HP.")
            sleep(1.5)
            print("You launched your sword into Eggrie's chest, Eggrie lost 100 HP, he died.")
            sleep(1.5)
            print("You healed 20 HP and gained experience.")
            sleep(1.5)
            print("You found the Wooden gem.")
        gems_found += 1
        walkway = int(input("Where do you want to go? (1, the Forbidden Forest. 2, the Warping Realm. 3, the Magical lake.)"))
        if fight == "no":
            print("You ran away.")
            sleep(1.5)
            print("You met a lot of Woodlanders. Game over.")
            game_over = True
            quit
    if gems_found == 3:
        print("You won! You also saved the princess!")
        quit
    elif walkway == 2:
        print("Heading to the Warping Realm...")
        sleep(2.5)
        print("You met a Warper, blocking you from the way to the Warper Gem.")
        print("Beben\nAttack: 9\nDefense: 6\nWeapon: None\nSkill: Warping Hit")
        fight2 = input("Would you like to fight? (Yes/no)")
        if fight2 == "yes":
            print("FIGHT!")
            sleep(1.5)
            print("Beben launched a warping hit from behind. You lost 35 HP.")
            sleep(1.5)
            print("You launched your sword at Beben's leg, he lost 60 HP.")
            sleep(1.5)
            print("Beben struggled but managed to land another warping hit straight to your arm. You lost 30 HP.")
            sleep(1.5)
            print("You pierced Beben with your sword into the head. Beben died.")
            sleep(1.5)
            print("You ate a nearby warping pill and regained 100 HP.")
            sleep(1.5)
            print("You found the warper gem.")
            gems_found += 1
            walkway = int(input("Where do you want to go? (1, the Forbidden Forest. 2, the Warping Realm. 3, the Magical lake.)"))
        if fight2 == "no":
            print("You ran away and got caught by Beben. He tortured you with his warping hits and killed you. Game over.")
            game_over = True
            quit
    if gems_found == 3:
        print("You won! You also saved the princess!")
        quit
    elif walkway == 3:
        print("Heading to the magical lake...")
        sleep(2.5)
        print("A Lakeviewer pushed you into the lake, affecting you with enormous amounts of boost.")
        sleep(2.5)
        print(name, "\nAttack: 10 -> 25\nDefense: 8 -> 14\nWeapon: Sword -> OneHell Blade")
        sleep(2.5)
        print("Crackerjack: Heh, that's what you get for entering our territory, Jepprie!\nUs Lakeviewers don't allow Jeppries to enter.\nI'm Crackerjack, and I'm gonna finish you off.")
        sleep(2.5)
        print(name, ": We'll see about that.")
        sleep(2.5)
        fight3 = input("Would you like to fight? (yes/no)")
        if fight3 == "yes":
            print("FIGHT!")
            sleep(1.5)
            print("Crackerjack bombarded you with consecutive punches, it was too quick you couldn't analyze. You lost 40 HP.")
            sleep(1.5)
            print("You conjured up a large red cloud, sending red lightning down to Crackerjack. Crackerjack lost 80 Armor.")
            sleep(1.5)
            print("Crackerjack was about to kick you in the face, but you counter hit him. He got flung far away and lost 20 Armor, 15 HP.")
            sleep(1.5)
            print("Analyzing Crackerjack...")
            sleep(3)
            print("Crackerjack\nAttack: 19\nDefense: 11\nWeapon: Magic\nSkill: Magic Spells/Consecutive Punches")
            sleep(1.5)
            print("Crackerjack: Ugh, ugh, I'll still defeat you with every bit of my strength!")
            sleep(1.5)
            print(name, ": Wait what?-\nYou got hit in the back, sending you into a magical tree. You lost 50 HP.")
            sleep(1.5)
            print("Crackerjack: You're the strongest person I've ever met, but, the difference is far.")
            sleep(1.5)
            print(name, ": Huh? AAAAAAAAA-\nYou got sent into the lake again.")
            sleep(1.5)
            print("You gained bigger boosts and got side effects.")
            sleep(1.5)
            print(name, "\nAttack: 25 -> 35\nDefense: 14 -> 20\nWeapon: OneHell Blade -> Heavenly Blade")
            print("Side effects: Nausea, Dizziness.")
            sleep(5)
            print("Crackerjack: You'll stand no chance.\nYou got hit by Crackerjack, but something blocked the punch.")
            sleep(1.5)
            print("AN INVISIBLE SHIELD! The Heavenly Blade blocked the punch.")
            sleep(1.5)
            print("Crackerjack: GRR! Nobody can stop my punches!")
            sleep(1.5)
            print("Crackerjack punched a lot, but you recovered and threw the sword straight into Crackerjack's shoulder. He lost 25 HP.")
            sleep(1.5)
            print(name, ": You will die.")
            sleep(1.5)
            print("You slashed Crackerjack's head. He died.")
            sleep(3)
            print("You found the magical gem.")
            walkway = int(input("Where do you want to go? (1, the Forbidden Forest. 2, the Warping Realm. 3, the Magical lake.)"))
            gems_found += 1
        elif fight3 == "no":
            print("You got punched in the skull by Crackerjack, you died. Game over.")
            game_over = True
            quit
    if gems_found == 3:
        print("You won! You also saved the princess!")
        quit
