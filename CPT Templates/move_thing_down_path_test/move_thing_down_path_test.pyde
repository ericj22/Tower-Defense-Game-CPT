circle_x = 400
circle_y = 0
x = [400, 400]
y = [-100, -200]

def setup():
    size(1280, 720)
    noStroke()

def draw():
    background("#D6EDFF")
    drawTarget()
    drawCircle()
    
def drawTarget():
    fill(240, 0, 0)
    rect(775, 560, 50, 50)
    
def drawCircle():
    fill("#478978")
    global circle_x, circle_y, x, y
    
    for i in range(len(y)):
        ellipse(x[i], y[i], 5, 5)
        if x[i] == 400 and y[i] <= 500:
            y[i] += 2
        if y[i] >= 500 and x[i] >= 400 and x[i] <= 600:
            x[i] += 1
            y[i] = -0.01*(x[i]-500)**2 + 600
        if y[i] >= 260 and x[i] == 600:
            y[i] -= 2
            print(x[i])
        if y[i] <= 260 and x[i] >= 600:
            x[i] += 1
            y[i] = 0.01*(x[i]-700)**2 + 160
        if x[i] >= 800:
            y[i] += 2
    
    fill(255)
    ellipse(circle_x, circle_y, 50, 50)
    if circle_y <= 500 and circle_x == 400:
        circle_y += 2
    if circle_y >= 500 and circle_x >= 400 and circle_x <= 600:
        circle_x += 1
        circle_y = -0.01*(circle_x-500)**2 + 600
    if circle_y >= 260 and circle_x == 600:
        circle_y -= 2
    if circle_y <= 260 and circle_x >= 600:
        circle_x += 1
        circle_y = 0.01*(circle_x-700)**2 + 160
    if circle_x >= 800:
        circle_y += 2
    
