import time
from enemy import Enemy


class Tower:
    """
    Class for the towers in the game
    Note: The coordinates are represented with individual variables, because for
    some reason the objects cannot keep their own independent values in arrays
    """
    type = ""
    tier = 1
    tower_range = -1
    enemy_targeted = False
    xLoc = -1
    yLoc = -1
    projectileX = -1
    projectileY = -1
    projectile_speed = -1
    damage = -1
    m = -1
    b = -1
    targeted_enemy = None
    targetX = -1
    targetY = -1
    test_enemy = None
    is_selected = False
    upgrade_cost = -1
    time_hit = -1

    def upgrade(self):
        """
        Upgrades a tower's stats
        """
        pass

    def find_enemy(self, enemies):
        """
        Takes a list of enemies and searches through them to find an enemy in range
        Sets the tower's targeted enemy to the enemy in range
        """
        for enemy in enemies:
            if sqrt((enemy.xLoc-self.xLoc)**2 + (enemy.yLoc-self.yLoc)**2) <= self.tower_range:
                self.targeted_enemy = enemy
                return
        self.targeted_enemy = None

    def target_enemy(self):
        """
        Once an enemy is found, the function determines where the enemy will
        be by the time the projectile hits the enemy.
        The function then uses its own coordinates the projected location of the
        enemy to determine the slope and y or x intercepts of a linear equation
        """
        if self.targeted_enemy.xLoc <= 563:  # Targets enemies moving vertically, with y = mx+b (x as independent variable)
            distance = abs(self.xLoc-self.targeted_enemy.xLoc)
            self.targetX = self.targeted_enemy.xLoc
            self.targetY = self.targeted_enemy.yLoc + (distance/self.projectile_speed)*self.targeted_enemy.speed
            try:
                self.m = float(float(self.targetY - self.yLoc)/float(self.targetX-self.xLoc))  # Slope
            except:
                self.targeted_enemy = None
                self.enemy_targeted = False
                return
            self.b = float(self.yLoc - self.xLoc*self.m)  # y-intercept
        else:  # Targets enemies moving horizontally, with x = my + b (y as independent variable)
            distance = abs(self.yLoc-self.targeted_enemy.yLoc)
            self.targetX = self.targeted_enemy.xLoc + (distance/self.projectile_speed)*self.targeted_enemy.speed
            self.targetY = self.targeted_enemy.yLoc
            try:
                self.m = float(float(self.targetX-self.xLoc)/float(self.targetY - self.yLoc))  # Slope
            except:
                self.targeted_enemy = None
                self.enemy_targeted = False
                return
            self.b = float(self.xLoc - self.yLoc*self.m)  # x-intercept
        self.enemy_targeted = True

    def shoot_projectile(self):
        """
        Using the slope and y or x intercept from the target_enemy function,
        this function draws a projectile starting from it's own coordinates and makes
        the projectile follow the line of the equation determined in the target_enemy
        function
        """
        fill(255)
        ellipse(round(self.projectileX), round(self.projectileY), 6, 6)
        # Used different movement patterns for the projectile based on the tower's location relative to the enemy
        if self.targeted_enemy.yLoc < 320 and self.xLoc < self.targeted_enemy.xLoc:
            self.projectileX += self.projectile_speed
            self.projectileY = self.m*self.projectileX + self.b
        elif self.targeted_enemy.yLoc < 320:
            self.projectileX -= self.projectile_speed
            self.projectileY = self.m*self.projectileX + self.b
        elif self.yLoc < self.targeted_enemy.yLoc:
            self.projectileY += self.projectile_speed
            self.projectileX = self.m*self.projectileY + self.b
        elif self.yLoc > self.targeted_enemy.yLoc:
            self.projectileY -= self.projectile_speed
            self.projectileX = self.m*self.projectileY + self.b

    def detect_enemy_hit(self):
        """
        Detects collision of a projectile and an enemy, or if a projectile
        goes too far
        """
        enemy_xloc = int(round(self.targeted_enemy.xLoc))
        enemy_yloc = int(round(self.targeted_enemy.yLoc))
        if sqrt((self.projectileX - self.xLoc)**2 + (self.projectileY - self.yLoc)**2) > sqrt((self.targeted_enemy.xLoc-self.xLoc)**2 + (self.targeted_enemy.yLoc-self.yLoc)**2):
            # If the projectile is too far
            self.projectileX = self.xLoc  # Reset projectile location
            self.projectileY = self.yLoc  # ||
            self.enemy_targeted = False  # Reset tower targeting
            self.targeted_enemy = None  # ||
        elif round(self.projectileX) in range(enemy_xloc-3, enemy_xloc+3) and round(self.projectileY) in range(enemy_yloc-3, enemy_yloc+3):
            # Checks for collision with enemy
            self.projectileX = self.xLoc
            self.projectileY = self.yLoc
            self.targeted_enemy.health -= self.damage
            if self.type == "ice tower":
                self.targeted_enemy.is_slowed = True
                self.targeted_enemy.time_slowed = time.time() + self.slowing_time
            self.enemy_targeted = False
            self.targeted_enemy = None

    def show_range(self):
        """
        Draws the range of the tower
        """
        fill(255, 255, 51, 40)
        ellipse(self.xLoc, self.yLoc, 2*self.tower_range, 2*self.tower_range)
