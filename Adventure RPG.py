import random

print("Welcome new Adventurer!")
print("Before we begin our journey, please enter your details")

name = input("Please enter your name: ")

STR = 5
DEX = 5
INT = 5
HP = DEX * 3 + 10
MP = INT * 7
EVADE = (DEX * 7) / 100

remainingStats = 10

slimeHP = 20
slimeTACKLE = 5

playerWHACK = 5 + STR * 0.5
playerSLASH = 8 + STR * 0.6

body_HP = 0
head_HP = 0
weapon_HP = 0

gold = 0
weapon = "stick"
head = "empty"
body = "empty"
level = 1
exp = 0

hpPotion = 3
hpPotionHeal = 15

mp_potion = 3
mp_potion_mana = 20

str_potion = 2
str_potion_str = 10
str_temp = STR
str_flag = False

giantHP = 500
giantPOKE = 5
giantKICK = 15
giantBASH = 5

bleedFlag = False
bleedDamage = 3

escape_flag = False

gameRunning = True
while(gameRunning):
    print("~~~~~~~~~~~~~~~~~~~~")
    print("Commands available:")
    print("addstats: Add remaining stat upgrade points to your stats")
    print("viewstats: Updates and prints out all stats of player")
    print("shop: access the shop menu")
    print("startbattle: starts a battle with random monster in current zone")
    print("quit: Exits the game")
    print("~~~~~~~~~~~~~~~~~~~~")
    command = input("Please enter a command: ").lower()
    if command == "addstats" and remainingStats > 0:
        print("Remaining stat upgrade points: " + str(remainingStats))
        print("Type EXIT if you would like to return to the main menu")

        try:
            stat = input("Please enter which stat to increase: ( STR/DEX/INT ) ").upper()
            if stat != "EXIT":
                try:
                    statUsed = int(input("Enter the amount of points to add to stat: "))    

                    if statUsed <= remainingStats:
                        if stat == "STR":
                            STR += statUsed
                            remainingStats -= statUsed
                            print("new STR: " + str(STR))

                        elif stat == "DEX":
                            DEX += statUsed
                            remainingStats -= statUsed
                            print("new DEX: " + str(DEX))
                        elif stat == "INT":
                            INT += statUsed
                            remainingStats -= statUsed
                            print("new INT: " + str(INT))

                        else:
                            print("Invalid input. Please enter a valid number for the amount of points to add and/or a valid stat name (STR, DEX, INT) or type EXIT.")
                        print("Remaining stat upgrade points: " + str(remainingStats)) 
                    else:
                        print("You are trying to add more stats than you currently have.")
                        print("Remaining stat upgrade points: " + str(remainingStats))
                except ValueError:
                    print("Invalid input. Please enter a valid number for the amount of points to add and/or a valid stat name (STR, DEX, INT) or type EXIT.")
                    print("Remaining stat upgrade points: " + str(remainingStats))
            else:
                print("Returning to the main menu...")
        except ValueError:
            print("Invalid input. Please enter a valid stat name (STR, DEX, INT) or type EXIT.")
            print(" 5 Remaining stat upgrade points: " + str(remainingStats))
                        
    elif command == "viewstats":
        HP = (10 + DEX * 3) + weapon_HP + body_HP + head_HP
        MP = INT * 7
        EVADE = (DEX * 2) / 100
        playerWHACK = int(5 + STR * 0.5)
        playerSLASH = int(8 + STR * 0.6)
        print(name + "'s stats")
        print("1. Main Stats:")
        print("LEVEL: " + str(level))
        print("EXP: " + str(exp))
        print("STR: " + str(STR))
        print("DEX: " + str(DEX))
        print("INT: " + str(INT))
        print("HP: " + str(HP))
        print("MP: " + str(MP))
        print("EVADE: " + str(EVADE))
        print("2. Attack Stats:")
        print("WHACK: " + str(playerWHACK))
        print("SLASH: " + str(playerSLASH))
        print("3. Inventory Stats:")
        print("GOLD: " + str(gold))
        print("Weapon: " + str(weapon))
        print("Head Armour: " + str(head))
        print("Body Armour: " + str(body))
        print("HP Potions: " + str(hpPotion))
        print("MP Potions: " + str(mp_potion))
        print("STR Potions: " + str(str_potion))

    elif command == "startbattle":
        randomMonster = random.randint(1,3)
        if randomMonster == 1:
            currentMonster = "giant"
            monsterHP = giantHP
        else:
            currentMonster = "slime"
            monsterHP = slimeHP
            monsterAttack = slimeTACKLE
        currentPlayerHP = (10 + DEX * 3) + weapon_HP + body_HP + head_HP
        currentPlayerMP = MP
        while (currentPlayerHP > 0 and monsterHP > 0):
            print("Gideon's HP: " + str(currentPlayerHP))
            print("Gideon's MP: " + str(currentPlayerMP))
            print(currentMonster + " HP: " + str(monsterHP))
            print("Available battle commands:")
            print("Fight")
            print("Use Potion")
            print("Escape")
            battleCommand = input("Gideon's action: ")
            while battleCommand != "Fight" and battleCommand != "Use Potion" and battleCommand != "Escape":
                print("Invalid, try again.") 
                battleCommand = input("Gideon's action: ")
            if battleCommand == "Fight":
                if str_flag:
                    print("Attack 1: WHACK (0MP) | DMG: " + str(playerWHACKe))
                    print("Attack 2: SLASH (5MP) | DMG: " + str(playerSLASHe))
                else:
                    print("Attack 1: WHACK (0MP) | DMG: " + str(playerWHACK))
                    print("Attack 2: SLASH (5MP) | DMG: " + str(playerSLASH))
                print("Type QUIT to return to battle command menu")
                attack = input("Choose attack number: ")
                if attack == "1":
                    if str_flag == True:
                        print("using Power Whack")
                        monsterHP -= playerWHACKe
                    else:
                        print("using Normal Whack")
                        monsterHP -= playerWHACK
                        
                elif attack == "2":
                    if currentPlayerMP >= 5:
                        if str_flag == True:
                            print("using Power Slash")
                            monsterHP -= playerSLASHe
                        else:
                            print("using Normal Slash")
                            monsterHP -= playerSLASH
                        currentPlayerMP -= 5
                        if currentPlayerMP <= 0:
                            currentPlayerMP = 0
                    else:
                        print("Gideon does not have enough MP to perform this attack")
                        continue
                elif attack == "QUIT":
                    continue
                else:
                    print("invalid command, pls try again.")
                    continue

            if battleCommand == "Use Potion":
                print("Potion choices: ")
                print("HP Potion | Heals Up To: " + str(hpPotionHeal)+ " HP | Amount Remaining: " + str(hpPotion))
                print("MP Potion | Restores: " + str(mp_potion_mana) + " Mana Points | Amount Remaining: " + str(mp_potion))
                print("STR Potion | Boosts: " + str (str_potion_str)+ " STR Stat Points | Amount Remaining: " + str(str_potion))
                print("Type QUIT to return to battle command menu")
                potionChoice = input("What potion to use: ")
                if potionChoice == "HP Potion":
                    currentPlayerHP += hpPotionHeal
                    hpPotion -= 1
                    bleedFlag = False
                    print("Gideon's HP has increased by up to " + str(hpPotionHeal) + " health")
                    if currentPlayerHP > HP:
                        if hpPotion > 0:
                            currentPlayerHP = HP
                    else:
                        print("Gideon does not have any HP Potions")
                elif potionChoice == "MP Potion":
                     currentPlayerMP += mp_potion_mana
                     mp_potion -= 1
                     print("Gideon's MP increased by up to " + str(mp_potion_mana))
                     if currentPlayerMP > MP:
                         if mp_potion_mana > 0:
                             currentPlayerMP = MP
                     else:
                         print("Gideon does not have any MP Potions")
                
                elif potionChoice == "STR Potion":
                    if str_potion > 0:
                        str_flag = True
                        STR += str_potion_str
                        str_temp = STR + 10
                        playerWHACKe = 5 + str_temp * 0.5
                        playerSLASHe = 8 + str_temp * 0.6
                        str_potion -= 1
                        print("Gideon's attack power has increased")
                    else:
                        print("Gideon does not have any STR Potions")
                elif potionChoice == "QUIT":
                    continue
                else:
                    print("invalid command, try again.")
                    continue

                    
            if battleCommand == "Escape":
                temp_evade = EVADE * 100
                random_evade = random.randint(0,100)
                if random_evade <= temp_evade:
                    escape_flag = True
                    print("Gideon has sucessfully escaped!")
                    str_flag = False
                    break
                else:
                    print("You are not able to run away from the battle.")

            if monsterHP > 0:
                if currentMonster == "slime":
                    monsterAttack = slimeTACKLE
                    print("Slime used TACKLE | DMG: " + str(monsterAttack))
                else:
                    randomAttack = random.randint(1,3)
                    if randomAttack == 1:
                        monsterAttack = giantPOKE
                        print("Giant used POKE | DMG: " + str(monsterAttack))
                    elif randomAttack == 2:
                        monsterAttack = random.randint(0,giantKICK)
                        print("Giant used KICK | DMG: " + str(monsterAttack))
                    else:
                        monsterAttack = giantBASH
                        print("Giant used BASH | DMG: " + str(giantBASH))
                        bleedFlag = True
                currentPlayerHP -= monsterAttack
                        
                if bleedFlag == True:
                    currentPlayerHP -= bleedDamage
                    print("Gideon took " +str(bleedDamage)+" damage from bleeding")
                    
            if currentMonster == "slime" and monsterHP < 0:
                print("Gideon defeated the " + currentMonster)
                gold += 10
                exp += 30
                str_flag = False
                print("Gold: " + str(gold))
                print("Exp: " + str(exp))
                
            if currentMonster == "giant" and monsterHP < 0:
                print("Gideon defeated the " + currentMonster)
                gold += 50
                exp += 150
                str_flag = False
                print("Gold: " + str(gold))
                print("Exp: " + str(exp))
                
            expToLevelUp = level * 50    
            if exp >= expToLevelUp:
                level += 1
                remainingStats += 5
                print("Gideon has levelled up!")
                print("Remaining upgrade stat points: " + str(remainingStats))
                print("Exiting to main menu...")
                    
            if currentPlayerHP <= 0:
                print("Gideon has failed to kill the " + currentMonster)
                gold -= 10
                exp += 5
                print("Exiting to main menu...")
                break
                
     
    elif command == "shop":
        print("weapon slot: dagger (20 gold)")
        print("weapon slot: mace (50 gold)")
        print("weapon slot: katana (70 gold)")
        print("head slot: cap (20 gold)")
        print("head slot: helmet (30 gold)")
        print("body slot: bronze armour (40 gold)")
        print("body slot: gold vest (60 gold)")
        print("potion slot: MP Potion (15 gold)")
        print("potion slot: HP Potion (20 gold)")
        print("potion slot: STR Potion (20 gold)")
        print("Type QUIT to Leave the Shop")
        itemToBuy = input("Select item to buy: ").lower()
        if itemToBuy == "dagger" and weapon != "dagger" and gold >= 20:
            weapon = "dagger"
            gold -= 20
            STR += 9
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "mace" and weapon != "mace" and gold >= 50:
            weapon = "mace"
            gold -= 50
            STR += 38
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "katana" and weapon != "katana" and gold >= 70:
            weapon = "katana"
            gold -= 70
            STR += 65
            print("HP: " + str(HP))
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "cap" and head != "cap" and gold >= 20:
            head = "cap"
            gold -= 20
            head_HP += 10
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "helmet" and head != "helmet" and gold >= 30:
            head = "helmet"
            gold -= 30
            head_HP += 20
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "bronze armour" and body != "bronze armour" and gold >= 40:
            body = "bronze armour"
            gold -= 40
            body_HP += 40
            print("HP: " + str(HP))
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "gold vest" and body != "gold vest" and gold >= 60:
            body = "gold vest"
            gold -= 60
            body_HP += 55
            print("HP: " + str(HP))
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "hp potion" and gold >= 20:
            gold -= 20
            hpPotion += 1
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "mp potion" and gold >= 15:
            gold -= 15
            mp_potion += 1
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "str potion" and gold >= 20:
            gold -= 20
            str_potion += 1
            print("Gideon bought the " + str(itemToBuy) + "!")
            print("gold remaining: " + str(gold))
        elif itemToBuy == "quit":
            print("Quitting Shop...")
        else:
            print("Sorry, you do not have enough gold to buy " + itemToBuy)
    
    
    elif command == "quit":
        gameRunning = False
        
    elif command == "1234567890":
        gold += 9999999
       

    else:
        print("Command is not recognized. Please enter a new command.\n")
