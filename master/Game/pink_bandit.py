from enemy import Enemy


class Pink_Bandit(Enemy):
    """
    Extends the Enemy class, basic class for the pink bandit enemy
    """
    def __init__(self, xLoc, yLoc):
        self.type = "pink bandit"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.health = 400
        self.weight = 1
        self.original_speed = 1.1
        self.speed = self.original_speed
        self.enemy_size = 17
        self.gold_worth = 63
        self.slowed_speed = 0.77

    def draw_enemy(self):
        """
        Draws the enemy, and changes colour depending
        on the status of the enemy
        """
        if self.is_invisible and self.is_slowed:
            fill(242, 135, 208, 40)
        elif self.is_invisible:
            fill(242, 135, 158, 40)
        elif self.is_slowed:
            fill(242, 135, 208)
        else:
            fill(242, 135, 158)
        ellipse(self.xLoc, self.yLoc, self.enemy_size, self.enemy_size)
