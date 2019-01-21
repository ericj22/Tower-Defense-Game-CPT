from enemy import Enemy


class Orange_Giant(Enemy):
    """
    Extends the Enemy class, basic class for the orange giant enemy
    """
    def __init__(self, xLoc, yLoc):
        self.type = "orange giant"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.health = 1500
        self.weight = 4
        self.original_speed = 0.6
        self.speed = self.original_speed
        self.enemy_size = 25
        self.gold_worth = 134
        self.slowed_speed = 0.42

    def draw_enemy(self):
        """
        Draws the enemy, and changes colour depending
        on the status of the enemy
        """
        if self.is_invisible and self.is_slowed:
            fill(255, 145, 103, 40)
        elif self.is_invisible:
            fill(255, 145, 43, 40)
        elif self.is_slowed:
            fill(255, 145, 103)
        else:
            fill(255, 145, 43)
        ellipse(self.xLoc, self.yLoc, self.enemy_size, self.enemy_size)
