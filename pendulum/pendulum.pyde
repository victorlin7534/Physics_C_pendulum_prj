L = g = ix = iy = x = y = t = theta = v = adjust_v = d_x = d_y = start = placed = reset = x_factor = y_factor = None
trail = {}
        
def draw():
    panel()
    global start,placed,ix,iy,reset,x,y,adjust_v,v,theta
    if keyPressed:
        if key == ENTER:
            start = True
            adjust_v = False
        if key == ' ':
            reset = True
        if adjust_v:
            if keyCode == UP:
                v += 0.1
            if keyCode == DOWN:
                v -= 0.1    
            if keyCode == LEFT:
                if theta >= 0.01:
                    theta -= 0.01
            if keyCode == RIGHT:
                if theta <= 2*PI - 0.01:
                    theta += 0.01
            drawArrow(ix,iy,v,theta)
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
    global L,g,d_x,d_y,x,y,theta,x_factor,y_factor,v
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
        if key == 't':
            x_factor += 0.01
        if key == 'g':
            x_factor -= 0.01
        if key == 'y':
            y_factor += 0.01
        if key == 'h':
            y_factor -= 0.01
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
    text(theta,125,900)
    text('x: ',200,900)
    text(x,225,900)
    text('y: ',350,900)
    text(y,400,900)
    text('x_factor: ',500,900)
    text(x_factor,600,900)
    text('y_factor: ',75,950)
    text(y_factor,150,950)
    text('v: ',225,950)
    text(v,275,950)
    popMatrix()
            
def setup():
    global L,g,ix,iy,t,d_x,d_y,start,placed,reset,x,y,theta,v,x_factor,y_factor, adjust_v
    size(800,1000)
    background(255)
    frameRate(120)
    L = 1
    g = 9.81
    x = y = ix = iy = t = d_y = d_x = theta = v = 0
    x_factor = y_factor = 1
    start = placed = reset = adjust_v = False
    trail.clear()
    
def pendulum():
    global g,L,t,ix,iy,d_x,d_y,theta,v,x,y,x_factor,y_factor
    w_x = sqrt(g/L)*x_factor
    w_y = sqrt(g/L)*y_factor
    pushMatrix()
    translate(400,400)
    x = (ix-400)*cos(w_x*t - d_x) + v*cos(theta)*sin(w_x*t) #if we set d_x or d_y, intial pos changes
    y = (iy-400)*cos(w_y*t - d_y) + v*sin(theta)*sin(w_y*t) #confirm if vtrig(t)sin(w) is correct
    t += 0.0025
    fill(0)
    ellipse(x,y,20,20)
    line(0,0,x,y)
    trail[x] = y #if time, find efficient trail recorder
    for x in trail:
        point(x,trail[x])
    popMatrix()
        
def mouseClicked():
    global ix,iy,placed,x,y,adjust_v
    if not placed:
        x = ix = mouseX 
        y = iy = mouseY
        placed = True
        adjust_v = True        

def mouseMoved():
    if not placed and not start:
        fill(0)
        ellipse(mouseX,mouseY,20,20)
        line(400,400,mouseX,mouseY)
        
def drawArrow(x,y,l,angle):
    pushMatrix()
    translate(x, y)
    rotate(angle)
    line(0,0,l, 0)
    if l >= 0:
        line(l, 0, l - 8, -8)
        line(l, 0, l - 8, 8)
    else:
        line(l, 0, l + 8, 8)
        line(l, 0, l + 8, -8)
    popMatrix()
        
    
    
