from position import Position

class Item:
    def __init__(self, name, attack, defense, x , y):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.pos = Position(x, y)
        self.is_equipped = False
