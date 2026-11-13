class Player:
    def __init__(self, hp = 12, mp = 4):
        self.max_hp = hp
        self.actual_hp = hp
        self.max_mp = mp
        self.actual_mp = mp

    # hp logic
    # simple damage function
    def take_dmg(self, damage):
        self.actual_hp -= damage

    # healing function
    def healing(self, heal):
        # if the heal amount is bigger then the max hp, the heal value turns into the max hp
        if heal > self.max_hp:
            heal = self.max_hp

        # in case that if the healing be negative
        if heal < 0:
            heal = 0

        # heal the amount of the healing, but after heal, if the value of the actual hp is bigger then the max hp, the actual hp value turns into the max hp
        # min returns the minimun value between the A and B
        self.actual_hp = min(self.actual_hp + heal, self.max_hp)

    def recover_hp(self):
        self.actual_hp = self.max_hp

    # every time that the max hp increases the actual hp increases to max
    def increase_max_hp(self, hp):
        self.max_hp = hp
        self.actual_hp = self.max_hp

    # mp logic
    # simple mp cast function
    def lose_mp(self, mp):
        self.actual_mp -= mp

    # mp regen function
    def mp_regen(self, mp):
        # if the mp amount is bigger then the max mp, the heal value turns into the max mp
        if mp > self.max_mp:
            mp = self.max_mp

        # in case that if the regn be negative
        if mp < 0:
            mp = 0

        # heal the amount of the regen, but after regen, if the value of the actual mp is bigger then the max mp, the actual mp value turns into the max mp
        # min returns the minimun value between the A and B
        self.actual_mp = min(self.actual_mp + mp, self.max_mp)

    def mp_recovery(self):
        self.actual_mp = self.max_mp

    # every time that the max mp increases the actual mp increases to max
    def increase_max_mp(self, mp):
        self.max_mp = mp
        self.actual_mp = self.max_mp


def display_bars(bars):
    def calc_filled_empty(max_hp, actual_hp, bar_width):
        filled = round(actual_hp / max_hp * bar_width)
        empty = bar_width - filled

        return filled, empty

    bar_width = 20

    top = []
    titles = []
    values = []
    bottom = []
    for name, max_value, actual_value in bars:
        filled, empty = calc_filled_empty(max_value, actual_value, bar_width)
    
        top.append("+" + "-"*(bar_width+2) + "+")
        titles.append(f"| {f'{name}':^{bar_width}} |")
        values.append("| " + "/" * filled + " " * empty + " |")
        bottom.append("+" + "-"*(bar_width+2) + "+")

    print("   ".join(top))
    print("   ".join(titles))
    print("   ".join(values))
    print("   ".join(bottom))



player = Player()
player.increase_max_hp(75)
player.increase_max_mp(25)

player.take_dmg(60)
player.lose_mp(10)

bars = [
    ('HEALTH', player.max_hp, player.actual_hp),
    ('MANA', player.max_mp, player.actual_mp),
]


display_bars(bars)