import math

class Tower:
    name = ""
    tier = 1
    tower_range = -1
    enemy_targeted = False
    xLoc = -1
    yLoc = -1
    projectile = []
    fire_rate = -1
    damage = -1
    m = -1
    b = -1
    targeted_enemy = None
    target = []
        
    def __init__(self, name, xLoc, yLoc):
        self.name = name
        if self.name == "square":
            self.tower_range = 90
            self.fire_rate = 2
            self.damage = 65
        if self.name == "circle":
            self.tower_range = 100
            self.fire_rate = 3
            self.damage = 25
        self.xLoc = xLoc
        self.yLoc = yLoc
        self.projectile.append(self.xLoc)
        self.projectile.append(self.yLoc)
    
    def upgrade(self):
        self.tier += 1
        if self.name == "square":
            self.damage += self.damage*0.25
            self.fire_rate += 1
        if self.name == "circle":
            self.tier += 1
            self.damage += self.damage*0.25
            self.fire_rate += 1
            
    def find_enemy(self, enemies):
        for i in range(len(enemies)):
            if math.sqrt((enemies[i].xLoc-self.xLoc)**2 + (enemies[i].yLoc-self.yLoc)**2) <= self.tower_range:
                print("Enemy Targeted!")
                self.targeted_enemy = enemies[i]
        return
    
    def target_enemy(self):
        if self.targeted_enemy.yLoc <= 300: #change this number based on hard coded tower range
            self.target.append(self.targeted_enemy.xLoc)
            print(self.targeted_enemy.yLoc)
            self.target.append(self.targeted_enemy.yLoc + (abs((self.xLoc-self.targeted_enemy.xLoc)/1.2)))
            print(self.target[0], self.target[1])
        elif self.targeted_enemy.yLoc > 320 and self.targeted_enemy.xLoc != self.xLoc:
            self.target.append((self.xLoc - self.targeted_enemy.xLoc)/2)
            self.target.append(6*(math.sqrt(self.target[0]-560))+316)
        self.m = float(float(self.target[1] - self.yLoc)/float(self.target[0]-self.xLoc))
        print(self.m)
        self.b = float(self.yLoc - self.xLoc*self.m)
        self.enemy_targeted = True
        
        
    def attack_enemy(self):
        fill(255)
        ellipse(round(self.projectile[0]), round(self.projectile[1]), 6, 6)
        self.projectile[0] += 1.2
        self.projectile[1] = self.m*self.projectile[0] + self.b
        if math.sqrt((self.targeted_enemy.xLoc-self.xLoc)**2 + (self.targeted_enemy.yLoc-self.yLoc)**2) > self.tower_range:
            self.targeted_enemy = None
            self.enemy_targeted = False
            self.projectile.pop(1)
            self.projectile.pop(0)
        #if projectile goes out of range of the path:
            #reset projectile to tower location
            #set enemy_targeted to false
        elif round(self.projectile[0]) == self.targeted_enemy.xLoc and round(self.projectile[1]) == self.targeted_enemy.yLoc:
            self.projectile[0] = self.xLoc 
            self.projectile[1] = self.yLoc
            self.targeted_enemy.health -= self.damage
            self.enemy_targeted = False
            self.targeted_enemy = None
            
    
    def draw_tower(self):
        if self.name == "circle":
            if self.tier == 1:
                fill(1, 139, 0)
            if self.tier == 2:
                fill(1, 156, 79)
            if self.tier == 3:
                fill(1, 184, 110)
            ellipse(self.xLoc, self.yLoc, 40, 40)
        if self.name == "square":
            if self.tier == 1:
                fill(204, 12, 2)
            if self.tier == 2:
                fill(199, 0, 34)
            if self.tier == 3:
                fill(142, 0, 32)
            ellipse(self.xLoc-50, self.yLoc-50, 40, 40)
