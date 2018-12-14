RANGE = 100
enemy_x = [740]
enemy_y = [-5]
projectile_x = 660
projectile_y = 300
attacking_enemy = False

def setup():
    size(1280, 720)
    noStroke()


def draw():
    background("#D4D2A5")
    buildTower()
    drawPath()
    drawEnemy()
    hitEnemy()
    
def buildTower():
    global RANGE, attacking_enemy
    fill("#3A445D")
    ellipse(660, 300, 50, 50)
    if len(enemy_x) > 0 and len(enemy_y) > 0:
        if enemy_x[0] in range(660-RANGE, 660+RANGE) and enemy_y[0] in range(300-RANGE, 300+RANGE):
            attacking_enemy = True

def drawPath():
    fill(255)
    rect(700, -5, 100, 720)

def drawEnemy():
    fill(240, 40, 40)
    global enemy_y, enemy_x
    ellipse(enemy_x[0], enemy_y[0], 10, 10)
    enemy_y[0] += 1
    
def hitEnemy():
    global projectile_x, projectile_y, attacking_enemy, enemy_x, enemy_y
    fill("#928779")
    if(attacking_enemy):
        target_y = enemy_y[0] + 8
        ellipse(projectile_x, projectile_y, 6, 6)
        projectile_y = -1.15*projectile_x+1059
        projectile_x += 1
        if projectile_x == enemy_x[0] and projectile_y == target_y:
            enemy_x.remove(0)
            enemy_y.remove(0)
            attacking_enemy = False
        
