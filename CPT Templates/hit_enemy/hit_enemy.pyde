RANGE = 100
enemy_x = [740, 740, 740]
enemy_y = [-5, -50, -100]
projectile_x = 660
projectile_y = 300
attacking_enemy = False
enemy_killed = True
en_x = 740
en_y = 200

def setup():
    size(1280, 720)
    noStroke()


def draw():
    background("#D4D2A5")
    buildTower()
    drawPath()
    if len(enemy_x) > 0:
        drawEnemy()
    hitEnemy()
    
def buildTower():
    global RANGE, attacking_enemy
    fill("#3A445D")
    ellipse(660, 300, 50, 50)
    if len(enemy_x) > 0 and len(enemy_y) > 0:
        if enemy_x[0] in range(660-RANGE, 660+RANGE) and enemy_y[0] in range(300-RANGE, 300+RANGE):
            attacking_enemy = True
            enemy_killed = False

def drawPath():
    fill(255)
    rect(700, -5, 100, 720)

def drawEnemy():
    fill(240, 40, 40)
    global enemy_y, enemy_x
    for i in range(len(enemy_y)):
        ellipse(enemy_x[i], enemy_y[i], 10, 10)
        enemy_y[i] += 1
        
def targetEnemy():
    global en_y, enemy_y, en_x, attacking_enemy, enemy_killed
    if(attacking_enemy and enemy_killed):
        en_y = enemy_y[0]
        print(en_x, en_y)
    
def hitEnemy():
    global projectile_x, projectile_y, attacking_enemy, enemy_x, enemy_y, en_x, en_y, enemy_killed
    fill("#928779")
    if(attacking_enemy):
        targetEnemy()
        target_y = enemy_y[0] + 80
        ellipse(projectile_x, projectile_y, 6, 6)
        m = float(findSlope(660, 300, en_x, en_y+80))
        print(m)
        b = findB(660, 300, m)
        projectile_y = m*projectile_x+b
        projectile_x += 1
        #print(projectile_x, floor(projectile_y), enemy_x[0], enemy_y[0])
        if projectile_x == enemy_x[0] and floor(projectile_y) == enemy_y[0]:
            enemy_x.pop(0)
            enemy_y.pop(0)
            projectile_x = 660
            projectile_y = 300
            attacking_enemy = False
            enemy_killed = True
        
def findSlope(x1, y1, x2, y2):
    y = float(y2 - y1)
    x = float(x2 - x1)
    return float(y/x)
    
def findB(x, y, m):
    return y - (x*m)
