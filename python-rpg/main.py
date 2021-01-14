from classes.game import person, bcolors
from classes.magic import spell
from classes.inventory import item

# black magic created
fire = spell("Fire", 15, 188, "black")
thunder = spell("Thunder", 12, 150, "black")
blizzard = spell("Blizzard", 10, 75, "black")
meteor = spell("Meteor", 20, 250, "black")
quake = spell("Quake", 12, 150, "black")

#create white magic
cure = spell("Cure", 12, 120, "white")
cura = spell("Cura", 20, 200, "white")


#create some items
potion = item("Potion", "potion", "Heals 20 HP", 50)
hiPotion = item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = item("Super Potion", "potion", "Heals 500 HP", 500)


#create some items
potion = item("Potion", "potion", "Heals 20 HP", 50)
hiPotion = item("Hi-Potion", "potion", "Heals 100 HP", 100)
superPotion = item("Super Potion", "potion", "Heals 500 HP", 500)

elixir = item("Elixir", "elixir", "Fully restores HP/MP of one party member", 9999)
hiElixir = item("Mega Elxir", "elixir", "Fully restores party's HP/MP", 9999)

grenade = item("Grenade", "attack", "Deals 500 damage", 500)

player_spells = [fire, thunder, blizzard, meteor, quake, cure, cura]
player_items = [potion, hiPotion, superPotion, elixir, hiElixir, grenade]

#Instantiate people
player = person(500, 50, 60, 35, player_spells, player_items)
enemy = person(1000, 65, 45, 25, [], [])

running = True
i = 0

print(bcolors.fail + bcolors.bold + "AN ENEMY ATTACKS!" + bcolors.endC)

while running:
    print("**********************************")
    player.choose_Action()
    choice = int(input("Choose action: "))
    choice = choice - 1

    # attack selection
    if choice == 0:
        damage = player.generate_Damage()
        enemy.take_damage(damage)
        print(bcolors.okGreen + "You attacked for", damage,"HP points." + bcolors.endC)
    # magic selection
    elif choice == 1:
        player.choose_Magic()
        magic_choice = int(input("Choose magic: ")) - 1
        
        if magic_choice == -1:
            continue

        spell = player.magic[magic_choice]
        magicDamage = spell.generate_Damage()
        current_mp = player.get_MP()

        if spell.cost > current_mp:
            print(bcolors.fail + "Not enough MP." + bcolors.endC)
            continue

        player.reduce_MP(spell.cost)
        
        if spell.type == "white":
            player.heal(magicDamage)
            print(bcolors.okBlue + "Spell: " + spell.name + ". Healed for " + str(magicDamage) + " HP." + bcolors.endC)    
        elif spell.type == "black":
            enemy.take_damage(magicDamage)
            print(bcolors.okBlue + "Spell: " + spell.name + ". Attacked for " + str(magicDamage) + " HP." + bcolors.endC)
    # inventory selection
    elif choice == 2:
        player.choose_Item()
        itemChoice = int(input("Choose item: ")) - 1 

        if itemChoice == -1:
            continue

        item = player.items[itemChoice]

        if item.type == "potion":
            player.heal(item.prop)
            print(bcolors.okBlue + item.name + " healed for " + str(item.prop) + " HP." + bcolors.endC)
        elif item.type == "elixir":
            player.heal(item.prop)
            player.healMP(item.prop)
            print(bcolors.okBlue + item.name + " increased HP & MP for max points." + bcolors.endC)
        elif item.type == "attack":
            enemy.take_damage(item.prop)
            print(bcolors.okGreen + "You attacked for", str(item.prop),"HP points." + bcolors.endC)
        
    
    enemy_choice = 1

    enemy_damage = enemy.generate_Damage()
    player.take_damage(enemy_damage)
    print(bcolors.fail + "Enemy attacked for", enemy_damage,"HP." + bcolors.endC)

    print("**********************************")

    print("Your HP:", bcolors.okGreen + str(player.get_HP()), "HP /", str(player.get_MaxHP()), "HP." + bcolors.endC)
    print("Your MP:", bcolors.okBlue, str(player.get_MP()), "MP/", str(player.get_MaxMP()), "MP." + bcolors.endC)
    print("Enemy HP:", bcolors.fail + str(enemy.get_HP()), "HP /", str(enemy.get_MaxHP()), "HP." + bcolors.endC)
    

    if enemy.get_HP() == 0:
        print(bcolors.okGreen + "You win!" + bcolors.endC)
        running = False
    elif player.get_HP() == 0:
        print(bcolors.fail + bcolors.bold + "\n\n\nYou lost!" + bcolors.fail)
        running = False