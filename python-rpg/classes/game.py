import random

class bcolors:
    header = '\033[95m'
    okBlue = '\033[94m'
    okGreen = '\033[92m'
    warning = '\033[93m'
    fail = '\033[91m'
    endC = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'
    

class person:
    def __init__(self, hp, mp, attack, defense, magic, items):
        self.maxHP = hp
        self.HP = hp
        self.maxMP = mp
        self.MP = mp
        self.attackLow = attack - 10
        self.attackHigh = attack + 10
        self.defense = defense
        self.magic = magic
        self.items = items
        self.actions = ["Attack", "Magic", "Items"]

    def generate_Damage(self):
        return random.randrange(self.attackLow, self.attackHigh)
    


    def take_damage(self, dmg):
        self.HP -= dmg
        if self.HP < 0:
            self.HP = 0
        return self.HP

    def heal(self, dmg):
        self.HP += dmg
        if self.HP > self.maxHP:
            self.HP = self.maxHP

    def healMP(self, dmg):
        self.MP += dmg
        if self.MP > self.maxMP:
            self.MP = self.maxMP

    def get_HP(self):
        return self.HP

    def get_MaxHP(self):
        return self.maxHP
    
    def get_MP(self):
        return self.MP

    def get_MaxMP(self):
        return self.maxMP

    def reduce_MP(self, cost):
        self.MP -= cost

    
    def choose_Action(self):
        i = 1
        print("\nActions")
        for item in self.actions:
            print("    " + str(i) + ":", item)
            i += 1

    def choose_Magic(self):
        i = 1
        print("\nMagic")
        for spell in self.magic:
            print("    " + str(i) + ":", spell.name, "cost:", str(spell.cost))
            i += 1

    def choose_Item(self):
        i = 1
        
        print("\n" + bcolors.okGreen + bcolors.bold + "Items:" + bcolors.endC)
        for item in self.items:
            print("    " + str(i) + ".", item.name, ":", item.description, " (x5)")
            i += 1