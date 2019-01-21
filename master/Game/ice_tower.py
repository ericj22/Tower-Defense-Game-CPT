from tower import Tower


class Ice_Tower(Tower):
    """
    A class extending the main tower class, is a different type of tower
    """
    slowing_time = -1

    def __init__(self, xLoc, yLoc):
        self.type = "ice tower"
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.tower_range = 85
        self.projectile_speed = 1.1
        self.damage = 40
        self.upgrade_cost = 120
        self.projectileX = xLoc
        self.projectileY = yLoc
        self.slowing_time = 1

    def upgrade(self):
        """
        Upgrades a tower's stats
        """
        self.tier += 1
        if self.tier == 2:
            self.damage = 50
            self.slowing_time += 0.5
            self.upgrade_cost = 200
            self.projectile_speed = 1.15
            self.tower_range += 10
        if self.tier == 3:
            self.damage = 60
            self.slowing_time += 1
            self.projectile_speed += 0.05
            self.tower_range += 15

    def draw_tower(self):
        """
        Draws the tower based upon its tier
        """
        if self.tier == 1:
            fill(107, 166, 229)
        if self.tier == 2:
            fill(142, 197, 255)
        if self.tier == 3:
            fill(187, 217, 249)
        ellipse(self.xLoc, self.yLoc, 40, 40)
