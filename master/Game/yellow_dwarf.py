from enemy import Enemy


class Yellow_Dwarf(Enemy):
    """
    Extends the Enemy class, basic class for the yellow dwarf enemy
    """
    def __init__(self, xLoc, yLoc):
        self.type = "yellow dwarf"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.health = 100
        self.weight = 1
        self.original_speed = 0.8
        self.speed = self.original_speed
        self.enemy_size = 15
        self.gold_worth = 36
        self.slowed_speed = 0.56

    def draw_enemy(self):
        """
        Draws the enemy, and changes colour depending
        on the status of the enemy
        """
        if self.is_invisible and self.is_slowed:
            fill(240, 255, 100, 40)
        elif self.is_invisible:
            fill(240, 255, 20, 40)
        elif self.is_slowed:
            fill(240, 255, 100)
        else:
            fill(240, 255, 20)
        ellipse(self.xLoc, self.yLoc, self.enemy_size, self.enemy_size)
