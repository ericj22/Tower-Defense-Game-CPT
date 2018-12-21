import random
circle_x = 400
circle_y = 0
x = []
for i in range(8):
    x.append(random.randint(376, 424))
y = [-100, -150, -125, -175, -200, -225, -250, -275]
pathDrawn = False

def setup():
    size(1280, 720)
    noStroke()
    #background("#D6EDFF")

def draw():
    background("#D6EDFF")
    drawCircle()

def drawCircle():
    fill("#478978")
    global circle_x, circle_y, x, y
    
    for i in range(len(y)-1, -1, -1):
        ellipse(x[i], y[i], 5, 5)
        if x[i] in range(375, 425) and y[i] <= 500:
            y[i] += 2
        if y[i] >= 500 and x[i] in range(375, 625):
            x[i] += 1
            y[i] = -0.01*(x[i]-500)**2 + 600
            x[i] += 1
            y[i] = -0.01*(x[i]-500)**2 + 600
        if y[i] >= 260 and x[i] in range(575, 625):
            y[i] -= 2
        if y[i] <= 260 and x[i] >= 575:
            x[i] += 1
            y[i] = 0.01*(x[i]-700)**2 + 160
            x[i] += 1
            y[i] = 0.01*(x[i]-700)**2 + 160
        if x[i] >= 775:
            y[i] += 1
            x[i] += 2
        if x[i] >= 1280:
            x.pop(i)
            y.pop(i)
    
    fill(255)
    ellipse(circle_x, circle_y, 50, 50)
    if circle_y <= 500 and circle_x == 400:
        circle_y += 2
    if circle_y >= 500 and circle_x >= 400 and circle_x <= 600:
        circle_x += 1
        circle_y = -0.01*(circle_x-500)**2 + 600
        circle_x += 1
        circle_y = -0.01*(circle_x-500)**2 + 600
    if circle_y >= 260 and circle_x == 600:
        circle_y -= 2
    if circle_y <= 260 and circle_x >= 600:
        circle_x += 1
        circle_y = 0.01*(circle_x-700)**2 + 160
        circle_x += 1
        circle_y = 0.01*(circle_x-700)**2 + 160
    if circle_x >= 800:
        circle_y += 1
        circle_x += 2
