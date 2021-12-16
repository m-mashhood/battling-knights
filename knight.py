from position import Position

class Knight:
    statuses = ('LIVE', 'DEAD', 'DROWNED')

    def __init__(self, name, y, x):
        self.name = name
        self.pos = Position(x, y)
        self.item = None
        self.status = self.statuses[0]
        self.base_attack = 1
        self.base_defense = 1

    def set_status(self, status_idx):
        self.status = self.statuses[status_idx]

    def get_total_attack_score(self):
        return self.base_attack + getattr(self.item, 'attack' , 0)

    def get_total_defense_score(self):
        return self.base_defense + getattr(self.item, 'defense' , 0)

    def is_alive(self):
        return self.status == self.statuses[0]

    def set_drowned(self):
        if self.item:
            self.item.is_equipped = False

        self.pos = None
        self.item = None
        self.status = self.statuses[2]
        self.base_attack = 0
        self.base_defense = 0

    def set_dead(self):
        if self.item:
            self.item.is_equipped = False

        self.item = None
        self.status = self.statuses[1]
        self.base_attack = 0
        self.base_defense = 0
