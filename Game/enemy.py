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
    
    def draw_enemy(self):
        if self.name == "red giant":
            fill(240, 40, 40)
            enemy_size = 30
        if self.name == "yellow dwarf":
            fill(240, 255, 20)
            enemy_size = 20
        ellipse(self.xLoc, self.yLoc, enemy_size, enemy_size)
