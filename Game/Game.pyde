import math
from enemy import Enemy
from tower import Tower

GOLD = 200
HEALTH = 20

enemies = []
yellow_dwarf = Enemy("yellow dwarf", 560, -10)
enemies.append(yellow_dwarf)
circle = Tower("circle", 500, 200)

def setup():
    size(1280, 720)
    noStroke()
    #background(0)


def draw():
    global enemies, circle
    background(0)
    enemies[0].draw_enemy()
    if enemies[0].yLoc <= 320:
        enemies[0].yLoc += 1
    else:
        enemies[0].xLoc += 1
        enemies[0].yLoc = 6*(math.sqrt(enemies[0].xLoc-560))+318
        
    circle.draw_tower()
    if circle.targeted_enemy != None and not circle.enemy_targeted:
        circle.target_enemy()
    elif circle.enemy_targeted:
        circle.attack_enemy()
    else:
        circle.find_enemy(enemies)
    
    
        
    #HAVE A TUNNEL SO TOWERS CAN SWITCH THEIR TARGETING
    #OR, THERE'S A WALL BLOCKING THE TARGETS
    #Nah, just hardcode it so that there's no way that they could target the other boys
