from tower import Tower


class Circle(Tower):
    """
    A class extending the main tower class, is a different type of tower
    """

    def __init__(self, xLoc, yLoc):
        self.type = "circle"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.tower_range = 85
        self.projectile_speed = 1.4
        self.damage = 35
        self.projectileX = xLoc
        self.projectileY = yLoc
        self.upgrade_cost = 110

    def upgrade(self):
        """
        Upgrades a tower's stats
        """
        self.tier += 1
        if self.tier == 2:
            self.damage = 45
            self.projectile_speed = 1.5
            self.upgrade_cost = 160
        if self.tier == 3:
            self.damage = 65
            self.projectile_speed += 0.2
        self.tower_range += 15

    def draw_tower(self):
        """
        Draws the tower based upon its tier
        """
        if self.tier == 1:
            fill(1, 139, 40)
        if self.tier == 2:
            fill(1, 156, 79)
        if self.tier == 3:
            fill(1, 166, 119)
        ellipse(self.xLoc, self.yLoc, 40, 40)
