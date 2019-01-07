import math

GOLD = 200
HEALTH = 20

def setup():
    size(1280, 720)
    


class Enemy:
    global HEALTH
    name = ""
    xLoc = -1
    yLoc = -1
    health = -1
    weight = -1
    
    def __init__(self, name, xLoc, yLoc):
        self.name = name
        self.xLoc = xLoc
        self.yLoc = yLoc
        if name == "yellow dwarf":
            self.weight = 1
            self.health = 100
        if name == "red giant":
            self.weight = 2
            self.health = 400
            
    def pass_course(self):
        global HEALTH
        HEALTH -= self.weight
        
    def check_living(self):
        if self.health <= 0:
            return False
        return True


class Tower:
    global GOLD
    name = ""
    tier = 1
    tower_range = -1
    enemy_targeted = False
    xLoc = -1
    yLoc = -1
    projectile = [[]]
    fire_rate = -1
    damage = -1
    m = -1
    b = -1
    
    def __init__(self, name, xLoc, yLoc):
        self.name = name
        if self.name == "square":
            self.tower_range = 100
            self.fire_rate = 2
            self.damage = 65
        if self.name == "circle":
            self.tower_range = 120
            self.fire_rate = 3
            self.damage = 25
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.projectile[0].append(self.xLoc)
    
    def upgrade(self):
        global GOLD
        self.tier += 1
        if self.name == "square":
            self.damage += self.damage*0.25
            self.fire_rate += 1
            GOld -= 100
        if self.name == "circle":
            self.tier += 1
            self.damage += self.damage*0.25
            self.fire_rate += 1
            GOLD -= 70
            
    def find_enemy(self, enemies):
        for i in range(len(enemies)):
            if math.sqrt((enemies[i].xLoc-self.xLoc)**2 + (enemies[i].xLoc-self.yLoc)**2) <= self.tower_range:
                self.enemy_targeted = True
                print("Enemy Targeted!")
                return enemies[i]
        return None
    
    def target_enemy(self, enemy):
        m = float(float(enemy.yLoc - self.yLoc)/float(enemy.xLoc-self.xLoc))
        b = float(self.yLoc - self.xLoc*m)
    
    def attack_enemy(self, enemy):
        fill(0)
        ellipse(projectile[0][0], projectile[0][1], 6, 6)
        self.projectile[0][0] += 1
        self.projectile[0][1] = self.m*self.xLoc + self.b
        #if projectile goes out of range of the path:
            #reset projectile to tower location
            #set enemy_targeted to false
        if self.projectile[0][0] == enemy.xLoc and self.projectile[0][1] == enemy.yLoc:
            self.projectile[0].pop(0)
            self.projectile[0].pop(1)
            enemy.health -= self.damage
    
    def draw_tower(self):
        if self.name == "circle":
            if self.tier == 1:
                colour = (1, 139, 0)
            if self.tier == 2:
                colour = (1, 156, 79)
            if self.tier == 3:
                colour = (1, 184, 110)
            fill(colour)
            ellipse(self.xLoc, self.yLoc, 100, 100)
        if self.name == "square":
            if self.tier == 1:
                colour = (204, 12 2)
            if self.tier == 2:
                colour = (199, 0, 34)
            if self.tier == 3:
                colour = (142, 0, 32)
            fill(colour)
            ellipse(self.xLoc-50, self.yLoc-50, 100, 100)
    
            
