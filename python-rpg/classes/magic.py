import random

class spell:
    def __init__(self, name, cost, damage, type):
        self.name = name
        self.cost = cost
        self.damage = damage
        self.type = type

    def generate_Damage(self):
        low = self.damage - 15
        high = self.damage + 15
        return random.randrange(low, high)