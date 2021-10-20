from vpython import *
g=9.8             #g = 9.8 (m/s**2)
size=0.25         #radius of the ball
C_drag = 0.9      #drag Coefficient (assume the correlation is linear)
theta = pi/3     #the elevation angle of velocity
constant = 0.3    #the constant between the length of arrow and the velocity of ball
dt = 0.001        #the real time elapses in one step in the while loop.

bouncing_time = 0 #how many time the ball bounces
time = 0          #the horizontal value of the graph

x_displacement=0  #the x-axis displacement of the ball 
y_displacement=0  #the y-axis displacement of the ball 
total_distance=0  #total distance the ball travels 
height = 0        #the hightest height of the ball
last_v_y = 0      #record the y_velocity before dt

scene = canvas(width = 800 , height = 800 , align = 'left',  background=vec(0.5,0.5,0))
floor = box(length=30, height=0.3, width=10, color=color.blue)
ball = sphere(radius = size, color=color.red, make_trail = True, trail_radius=size/3)
a1 = arrow(color=color.green , shaftwidth = 0.3)

oscillation = graph(width = 500, align = 'right')
funct1 = gcurve(graph = oscillation, color=color.blue, width=2)

ball.pos = vec(-15, size, 0)                   #initial position of the ball
a1.pos = ball.pos                              #initial position of the arrow
ball.v = vec(20*cos(theta), 20*sin(theta), 0)  #initial velocity of the ball
a1.axis = constant * ball.v                    #initial axis of the arrow

#when the ball starts to move and bounces less then 3 times 
while bouncing_time<=10 :
    time+=1
    rate(1000)

    last_v_y = ball.v.y
    ball.v += vec(0,-g,0)*dt - C_drag*ball.v*dt
    ball.pos += ball.v*dt
    a1.pos = ball.pos
    a1.axis = constant * ball.v

    magnitude = sqrt( pow(ball.v.x,2) + pow(ball.v.y,2)) #the magnitude of speed
    funct1.plot ( pos=(time, magnitude) )
    total_distance += magnitude*dt
    x_displacement +=ball.v.x*dt
    y_displacement +=ball.v.y*dt

    #when the ball reach the hightest point
    if last_v_y>=0 and ball.v.y<=0:
        height = max(height , y_displacement)
        print(height)

    #when the ball hits the ground
    if ball.pos.y <= size and ball.v.y<0:
        bouncing_time += 1
        ball.v.y *= (-1)
        a1.axis = constant * ball.v

msg = text(text = 'the displacement of the ball= ' + str(x_displacement) + 'm', pos = vec(-20, 15, 0) )
msg = text(text = 'the total distance the ball travels = ' + str(total_distance) + 'm', pos = vec(-20, 12, 0) )
msg = text(text = 'the hightest height the ball reaches = ' + str(height) + 'm', pos = vec(-20, 9, 0))



