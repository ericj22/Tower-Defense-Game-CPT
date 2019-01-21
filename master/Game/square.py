from tower import Tower


class Square(Tower):
    """
    A class extending the main tower class, is a different type of tower
    """
    def __init__(self, xLoc, yLoc):
        self.type = "square"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.tower_range = 80
        self.projectile_speed = 1
        self.damage = 75
        self.projectileX = xLoc
        self.projectileY = yLoc
        self.upgrade_cost = 160

    def upgrade(self):
        """
        Upgrades a tower's stats
        """
        self.tier += 1
        self.tower_range += 15
        if self.tier == 2:
            self.damage = 165
            self.upgrade_cost = 240
        if self.tier == 3:
            self.damage = 285

    def draw_tower(self):
        """
        Draws the tower based upon its tier
        """
        if self.tier == 1:
            fill(204, 12, 2)
        if self.tier == 2:
            fill(199, 0, 34)
        if self.tier == 3:
            fill(142, 0, 32)
        rect(self.xLoc-20, self.yLoc-20, 40, 40)
