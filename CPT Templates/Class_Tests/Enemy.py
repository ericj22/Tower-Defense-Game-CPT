class Enemy:
    name = ""
    xLoc = -1
    yLoc = -1
    
    def __init__(self, xLoc, yLoc, name):
        self.name = name
        self.xLoc = xLoc
        self.yLoc = yLoc
        

goblin = Enemy(100, 100, "goblin")
print(goblin.xLoc, goblin.yLoc, goblin.name)
