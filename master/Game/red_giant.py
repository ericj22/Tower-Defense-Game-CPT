from enemy import Enemy


class Red_Orc(Enemy):
    """
    Extends main Enemy Class, basic class for the red orc
    Note: The file is named red_giant due to name changes during
    development
    """
    def __init__(self, xLoc, yLoc):
        self.type = "red orc"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.health = 380
        self.weight = 1
        self.original_speed = 0.8
        self.speed = self.original_speed
        self.enemy_size = 20
        self.gold_worth = 57
        self.slowed_speed = 0.56

    def draw_enemy(self):
        """
        Draws the enemy, and changes colour depending
        on the status of the enemy
        """
        if self.is_invisible and self.is_slowed:
            fill(240, 40, 120, 40)
        elif self.is_invisible:
            fill(240, 40, 40, 40)
        elif self.is_slowed:
            fill(240, 40, 120)
        else:
            fill(240, 40, 40)
        ellipse(self.xLoc, self.yLoc, self.enemy_size, self.enemy_size)
