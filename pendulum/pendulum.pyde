d = L = g = ix = iy = x = y = t = theta = v = adjust_v = d_x = d_y = start = placed = reset = x_factor = y_factor = None
trail = set()
        
def draw():
    panel()
    global start,placed,ix,iy,reset,x,y,adjust_v,v,theta
    if keyPressed:
        if key == ENTER:
            if placed:
                start = True
                adjust_v = False
        if key == ' ':
            reset = True
        if adjust_v:
            if keyCode == UP:
                v += 0.5
            if keyCode == DOWN:
                v -= 0.5    
            if keyCode == LEFT:
                if theta >= 0.01:
                    theta -= 0.01
            if keyCode == RIGHT:
                if theta <= TWO_PI - 0.01:
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
    global L,g,d_x,d_y,x,y,theta,x_factor,y_factor,v,start,d 
    if not start:
        if keyPressed:
            if key == 'w':   
                L += 1
            if key == 's':
                if L >= 1:
                    L -= 1
            if key == 'q':
                g += 0.01
            if key == 'a':
                if g >= 0.01:
                    g -= 0.01
            if key == 'e':
                if d_x <= HALF_PI - 0.001:
                    d_x += 0.001
            if key == 'd':
                if d_x >= 0.001:
                    d_x -= 0.001
            if key == 'r':
                if d_y <= HALF_PI - 0.001:
                    d_y += 0.001
            if key == 'f':
                if d_y >= 0.001:
                    d_y -= 0.001
            if key == 't':
                x_factor += 0.001
            if key == 'g':
                x_factor -= 0.001
            if key == 'y':
                y_factor += 0.001
            if key== 'h':
                y_factor -= 0.001
            if key == 'u':
                if d <= 0.9999:
                    d += 0.0001
            if key == 'j':
                if d >= 0.0001:
                    d -= 0.0001
    pushMatrix()
    fill(255)
    textSize(16)
    translate(0,0,-30)
    text('L: ',75,850)
    text(L,100,850)
    text('g: ',175,850)
    text(g,200,850)
    text('d_x: ',310,850)
    text(d_x,350,850)
    text('d_y: ',450,850)
    text(d_y,490,850)
    text('theta: ',75,900)
    text(theta,125,900)
    text('x: ',210,900)
    text(x,235,900)
    text('y: ',360,900)
    text(y,385,900)
    text('x_factor: ',510,900)
    text(x_factor,580,900)
    text('y_factor: ',75,950)
    text(y_factor,145,950)
    text('v: ',255,950)
    text(v,275,950)
    text('d: ',385,950)
    text(d,405,950)
    popMatrix()
            
def setup():
    global L,g,ix,iy,t,d_x,d_y,start,placed,reset,x,y,theta,v,x_factor,y_factor, adjust_v,d
    size(800,1000)
    background(255)
    frameRate(100)
    L = 100
    g = 9.81
    x = y = ix = iy = t = d_y = d_x = theta = v = d = 0
    x_factor = y_factor = 1
    start = placed = reset = adjust_v = False
    trail.clear()
    
def pendulum():
    global g,L,t,ix,iy,d_x,d_y,theta,v,x,y,x_factor,y_factor
    w_x = sqrt(g/L)*x_factor
    w_y = sqrt(g/L)*y_factor
    pushMatrix()
    translate(400,400)
    x = ((ix-400)*cos(w_x*t - d_x) + v*cos(theta)*sin(w_x*t - d_x))*exp(-d*t)
    y = ((iy-400)*cos(w_y*t - d_y) + v*sin(theta)*sin(w_y*t - d_y))*exp(-d*t)
    t += 0.05 
    fill(0)
    ellipse(x,y,20,20)
    line(0,0,x,y)
    trail.add((int(x),int(y)))
    for i in trail:
        point(i[0],i[1])
    popMatrix()
        
def mouseClicked():
    global ix,iy,placed,adjust_v,x,y
    if not placed:
        if sqrt((mouseX-400)*(mouseX-400)+(mouseY-400)*(mouseY-400)) < L:
            x = ix = mouseX 
            y = iy = mouseY
            placed = True
            adjust_v = True

def mouseMoved():
    global L
    if not placed and not start:
        if sqrt((mouseX-400)*(mouseX-400)+(mouseY-400)*(mouseY-400)) < L:
            fill(0)
            ellipse(mouseX,mouseY,20,20)
            line(400,400,mouseX,mouseY)
        
def drawArrow(x,y,l,angle):
    pushMatrix()
    translate(x,y)
    rotate(angle)
    line(0,0,l, 0)
    if l >= 0:
        line(l, 0, l - 8, -8)
        line(l, 0, l - 8, 8)
    else:
        line(l, 0, l + 8, 8)
        line(l, 0, l + 8, -8)
    popMatrix()
        
    
    
