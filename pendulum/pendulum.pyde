L = g = ix = iy = x = y = t = theta = v = phi = d_x = d_y = start = placed = reset = None
trail = {}
        
def draw():
    panel()
    global start,placed,ix,iy,reset,x,y
    if keyPressed:
        if key == ENTER:
            start = True
        if key == ' ':
            reset = True
    if reset:
        setup()
        reset = False
    if start:
        pendulum()
    else:
        if placed:
            if iy < 800:
                fill(0)
                ellipse(x,y,20,20)
                line(400,400,x,y)            
            
def panel():
    background(255)
    fill(0)
    rect(0,800,799,999)
    global L,g,d_x,d_y,x,y,theta,phi
    if keyPressed:
        if key == 'w':   
            L += 0.1
        if key == 's':
            if L >= 0.1:
                L -= 0.1
        if key == 'q':
            g += 0.01
        if key == 'a':
            if g >= 0.01:
                g -= 0.01
        if key == 'e':
            if d_x <= HALF_PI - 0.01:
                d_x += 0.01
        if key == 'd':
            if d_x >= 0.01:
                d_x -= 0.01
        if key == 'r':
            if d_y <= HALF_PI - 0.01:
                d_y += 0.01
        if key == 'f':
            if d_y >= 0.01:
                d_y -= 0.01
    pushMatrix()
    fill(255)
    textSize(16)
    translate(0,0,-30)
    text('L: ',75,850)
    text(L,100,850)
    text('g: ',175,850)
    text(g,200,850)
    text('d_x: ',350,850)
    text(d_x,400,850)
    text('d_y: ',500,850)
    text(d_y,550,850)
    text('theta: ',75,900)
    #text(theta,100,900)
    text('phi: ',175,900)
    #text(phi,200,900)
    text('x: ',350,900)
    text(x,400,900)
    text('y: ',500,900)
    text(y,550,900)
    popMatrix()
            
def setup():
    global L,g,ix,iy,t,d_x,d_y,start,placed,reset,x,y
    size(800,1000)
    background(255)
    frameRate(100)
    L = 1
    g = 9.81
    x = y = ix = iy = t = d_y = d_x = theta = v = phi = 0
    start = placed = reset = False
    trail.clear()
    
def pendulum():
    global g,L,t,ix,iy,d_x,d_y,theta,v,phi,x,y
    w_x = sqrt(g/L)*3
    w_y = sqrt(g/L)*2
    #A = L*cos(phi)
    x = 200*cos(w_x*t - d_x) + ix# + v*cos(theta)*t
    y = 350*cos(w_y*t - d_y) + iy# + v*sin(theta)*t
    t += 0.0005
    fill(0)
    ellipse(x,y,20,20)
    line(400,400,x,y)
    trail[x] = y
    for x in trail:
        point(x,trail[x])
        
def mouseClicked():
    global ix,iy,placed,x,y
    if not placed:
        x = ix = mouseX 
        y = iy = mouseY
        placed = True

def mouseMoved():
    if not placed and not start:
        fill(0)
        ellipse(mouseX,mouseY,20,20)
        line(400,400,mouseX,mouseY)

        
    
    
