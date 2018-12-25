RANGE = 100
enemy_x = 740
enemy_y = [-5, -50, -85, -150, -151, -155, -157, -160]
projectile_x = 660
projectile_y = 300
attacking_enemy = False
enemy_killed = False
m = 0
b = 0
enemy_targeted = False

def setup():
    size(1280, 720)
    noStroke()


def draw():
    background("#D4D2A5")
    buildTower()
    drawPath()
    if len(enemy_y) > 0:
        drawEnemy()
    #if attacking_enemy and not enemy_killed:
    if attacking_enemy:
        if not enemy_targeted:
            targetEnemy()
        hitEnemy()
    
def buildTower():
    global RANGE, attacking_enemy
    fill("#3A445D")
    ellipse(660, 300, 50, 50)
    if len(enemy_y) > 0:
        if enemy_x in range(660-RANGE, 660+RANGE) and enemy_y[0] in range(300-RANGE, 300+RANGE):
            attacking_enemy = True
            #enemy_targeted = False
            #enemy_killed = False

def drawPath():
    fill(255)
    rect(700, -5, 100, 730)

def drawEnemy():
    fill(240, 40, 40)
    global enemy_y, enemy_x
    for i in range(len(enemy_y)):
        ellipse(enemy_x, enemy_y[i], 10, 10)
        enemy_y[i] += 1

def targetEnemy():
    global enemy_y, enemy_targeted, m, b
    m = float(float(enemy_y[0]+79-300)/float(enemy_x-660))
    b = float(300 - (660*m))
    print("enemy found!")
    enemy_targeted = True
    
def hitEnemy():
    global projectile_x, projectile_y, attacking_enemy, enemy_x, enemy_y, enemy_killed, m, b, enemy_targeted
    fill("#928779")
    target_y = enemy_y[0] + 80
    ellipse(projectile_x, projectile_y, 6, 6)
    #print(m)
    projectile_y = m*projectile_x+b
    projectile_x += 1
    #projectile_y = m*projectile_x+b
    #projectile_x += 1
    print(projectile_x, (projectile_y), enemy_x, enemy_y[0])
    if projectile_x >= 800:
        projectile_x = 660
        projectile_y = 300
        attacking_enemy = False
        enemy_targeted = False
        print(enemy_y[0])
    if projectile_x == enemy_x and round(projectile_y) in range(enemy_y[0]-1, enemy_y[0]+1):
        enemy_y.pop(0)
        projectile_x = 660
        projectile_y = 300
        attacking_enemy = False
        #enemy_killed = True
        enemy_targeted = False
